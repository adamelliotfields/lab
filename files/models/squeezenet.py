# SqueezeNet is a CNN architecture made up of "fire" modules composed of a squeeze convolutional
# layer followed by two expand convolutional layers. The squeeze layer reduces the number of input
# channels, while the expand layers apply a mix of 1x1 and 3x3 convolutions. The 1x1 convolutions
# capture channel-wise (local, individual channel) information, while the 3x3 convolutions capture
# spatial (global, cross-channel) information. Residual (skip) connections are used to connect
# layers with the same number of channels:
# * 128: fire2 → fire3
# * 256: fire4 → fire5
# * 384: fire6 → fire7
# * 512: fire8 → fire9
#
# Unlike many other CNNs, SqueezeNet does not use fully connected layers. After the final fire
# module, a convolutional layer with the number of filters equal to `n_classes` is used.
# Global average pooling reduces the `n_classes` feature maps to a single vector for softmax.
#
# I've made the following changes from the reference Caffe implementation:
# 1. ReLU activation is replaced by Swish (Mish and GELU are slower).
# 2. Glorot uniform initialization is replaced by He uniform initialization.
# 3. SGD with momentum (0.9) and weight decay (0.0002) is replaced by AdamW.
#
# https://arxiv.org/abs/1602.07360 (Iandola et al., 2016)
# https://github.com/pytorch/vision/blob/main/torchvision/models/squeezenet.py
from keras import Input, Model, activations, initializers, layers, optimizers


class Fire(layers.Layer):
    def __init__(self, filters, name=None):
        super().__init__(name=name)
        self.squeeze = layers.Conv2D(
            filters // 8,
            kernel_size=1,
            activation=activations.swish,
            bias_initializer=initializers.Zeros(),
            kernel_initializer=initializers.HeUniform(),
        )

        # expand filters get halved to keep the same number of total filters after concatenation
        self.expand_1x1 = layers.Conv2D(
            filters // 2,
            kernel_size=1,
            activation=activations.swish,
            bias_initializer=initializers.Zeros(),
            kernel_initializer=initializers.HeUniform(),
        )
        self.expand_3x3 = layers.Conv2D(
            filters // 2,
            kernel_size=3,
            padding="same",
            activation=activations.swish,
            bias_initializer=initializers.Zeros(),
            kernel_initializer=initializers.HeUniform(),
        )

    # join the squeeze and expand layers
    def call(self, inputs):
        x = self.squeeze(inputs)
        x1 = self.expand_1x1(x)
        x2 = self.expand_3x3(x)
        return layers.Concatenate()([x1, x2])


# classes and shape defaults to CIFAR-10
# set dropout to 0 to omit
def make_squeezenet(
    n_classes=10,
    input_shape=(32, 32, 3),
    dropout=0.5,
    loss="categorical_crossentropy",
):
    inputs = Input(input_shape)

    c1 = layers.Conv2D(
        64,
        3,
        strides=2,
        name="conv1",
        padding="same",
        activation=activations.swish,
        bias_initializer=initializers.Zeros(),
        kernel_initializer=initializers.HeUniform(),
    )(inputs)
    c1 = layers.MaxPooling2D(3, strides=2, name="pool1")(c1)

    f2 = Fire(128, name="fire2")(c1)
    #  ↕
    f3 = Fire(128, name="fire3")(f2)
    f3 = layers.Add()([f2, f3])
    f3 = layers.MaxPooling2D(3, strides=2, name="pool2")(f3)

    f4 = Fire(256, name="fire4")(f3)
    #  ↕
    f5 = Fire(256, name="fire5")(f4)
    f5 = layers.Add()([f4, f5])
    f5 = layers.MaxPooling2D(3, strides=2, name="pool3")(f5)

    f6 = Fire(384, name="fire6")(f5)
    #  ↕
    f7 = Fire(384, name="fire7")(f6)
    f7 = layers.Add()([f6, f7])

    # dropout after final fire module
    f8 = Fire(512, name="fire8")(f7)
    #  ↕
    f9 = Fire(512, name="fire9")(f8)
    f9 = layers.Add()([f8, f9])
    f9 = layers.Dropout(dropout)(f9)

    # gaussian initialization for final layer
    # activation after pooling
    c10 = layers.Conv2D(
        n_classes,
        name="conv10",
        kernel_size=1,
        activation=None,
        bias_initializer=initializers.Zeros(),
        kernel_initializer=initializers.RandomNormal(
            mean=0.0,
            stddev=0.01,
        ),
    )(f9)
    c10 = layers.GlobalAveragePooling2D()(c10)

    outputs = layers.Activation(activations.softmax)(c10)
    optimizer = optimizers.AdamW(
        weight_decay=0.004,
        learning_rate=0.002,
    )

    model = Model(inputs=inputs, outputs=outputs)
    model.compile(
        loss=loss,
        optimizer=optimizer,
        metrics=["accuracy"],
    )
    return model

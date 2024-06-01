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
# https://arxiv.org/abs/1602.07360 (Iandola et al., 2016)
# https://github.com/pytorch/vision/blob/main/torchvision/models/squeezenet.py
from keras import Input, Model, initializers, layers, saving


# https://keras.io/guides/serialization_and_saving
@saving.register_keras_serializable(name="Fire")
class Fire(layers.Layer):
    def __init__(self, filters, *, seed=42, name=None, activation="relu", **kwargs):
        super().__init__(name=name, **kwargs)
        self.filters = filters
        self.activation = activation
        self.squeeze = layers.Conv2D(
            filters // 8,
            kernel_size=1,
            activation=activation,
            name=f"{name}_squeeze",
            kernel_initializer=initializers.HeUniform(seed=seed),
        )
        self.expand_1x1 = layers.Conv2D(
            filters // 2,  # expand filters get halved to keep the same number of total filters
            kernel_size=1,
            activation=activation,
            name=f"{name}_expand_1x1",
            kernel_initializer=initializers.HeUniform(seed=seed),
        )
        self.expand_3x3 = layers.Conv2D(
            filters // 2,
            kernel_size=3,
            padding="same",
            activation=activation,
            name=f"{name}_expand_3x3",
            kernel_initializer=initializers.HeUniform(seed=seed),
        )

    def get_config(self):
        config = super().get_config()
        config.update({"filters": self.filters, "activation": self.activation})
        return config

    # join the squeeze and expand layers
    def call(self, inputs):
        x = self.squeeze(inputs)
        x1 = self.expand_1x1(x)
        x2 = self.expand_3x3(x)
        return layers.Concatenate()([x1, x2])


def get_squeezenet(
    seed=42,
    dropout=0.0,
    classes=1000,
    activation="relu",
    input_shape=(224, 224, 3),
):
    inputs = Input(input_shape)

    c1 = layers.Conv2D(
        64,
        3,
        strides=2,
        name="conv1",
        padding="same",
        activation=activation,
        kernel_initializer=initializers.HeUniform(seed=seed),
    )(inputs)
    c1 = layers.MaxPooling2D(3, strides=2, name="pool1")(c1)

    f2 = Fire(128, seed=seed, name="fire2", activation=activation)(c1)
    f3 = Fire(128, seed=seed, name="fire3", activation=activation)(f2)
    f3 = layers.Add()([f2, f3])
    f3 = layers.MaxPooling2D(3, strides=2, name="pool2")(f3)

    f4 = Fire(256, seed=seed, name="fire4", activation=activation)(f3)
    f5 = Fire(256, seed=seed, name="fire5", activation=activation)(f4)
    f5 = layers.Add()([f4, f5])
    f5 = layers.MaxPooling2D(3, strides=2, name="pool3")(f5)

    f6 = Fire(384, seed=seed, name="fire6", activation=activation)(f5)
    f7 = Fire(384, seed=seed, name="fire7", activation=activation)(f6)
    f7 = layers.Add()([f6, f7])

    # dropout after final fire module
    f8 = Fire(512, seed=seed, name="fire8", activation=activation)(f7)
    f9 = Fire(512, seed=seed, name="fire9", activation=activation)(f8)
    f9 = layers.Add()([f8, f9])
    f9 = layers.Dropout(dropout)(f9)

    # gaussian initialization for final layer
    # activation after pooling
    c10 = layers.Conv2D(
        classes,
        name="conv10",
        kernel_size=1,
        activation=None,
        kernel_initializer=initializers.RandomNormal(mean=0.0, seed=seed, stddev=0.01),
    )(f9)
    c10 = layers.GlobalAveragePooling2D(name="avgpool")(c10)

    outputs = layers.Activation("softmax" if classes > 1 else "sigmoid", name="activation")(c10)
    return Model(inputs=inputs, outputs=outputs, name="SqueezeNet")

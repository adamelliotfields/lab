# ResNet-18 is a 18-layer residual network. There are 17 convolutional layers and 1 fully connected
# layer (the "trainable" layers). The network is divided into stages. The first stage has 1
# convolutional layer and 1 max pooling layer. The rest of the stages have 2 residual blocks. Each
# residual block has 2 convolutional layers.
from keras import Input, Model, initializers, layers, saving


# https://keras.io/guides/serialization_and_saving
@saving.register_keras_serializable(name="ResidualBlock")
class ResidualBlock(layers.Layer):
    def __init__(
        self,
        filters,
        *,
        seed=42,
        name=None,
        projection=False,
        activation="relu",
        **kwargs,
    ):
        super().__init__(name=name, **kwargs)
        strides = 2 if projection else 1
        self.filters = filters
        self.activation = activation
        self.projection = projection

        self.conv1 = layers.Conv2D(
            filters,
            3,
            padding="same",
            strides=strides,
            name=f"{name}_conv1",
        )
        self.bn1 = layers.BatchNormalization(name=f"{name}_bn1")
        self.activation1 = layers.Activation(activation, name=f"{name}_activation1")
        self.conv2 = layers.Conv2D(
            filters,
            3,
            padding="same",
            name=f"{name}_conv2",
            kernel_initializer=initializers.HeUniform(seed=seed),
        )
        self.bn2 = layers.BatchNormalization(name=f"{name}_bn2")

        # projection layer to match dimensions
        if projection:
            self.downsample = layers.Conv2D(
                filters,
                1,
                strides=2,
                name=f"{name}_downsample",
                kernel_initializer=initializers.HeUniform(seed=seed),
            )
            self.bn3 = layers.BatchNormalization(name=f"{name}_bn3")
        else:
            self.downsample = None

    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "filters": self.filters,
                "activation": self.activation,
                "projection": self.projection,
            }
        )
        return config

    def call(self, inputs, training=False):
        x = self.conv1(inputs)
        x = self.bn1(x, training=training)
        x = self.activation1(x)
        x = self.conv2(x)
        x = self.bn2(x, training=training)

        if self.projection:
            residual = self.downsample(inputs)
            residual = self.bn3(residual, training=training)
        else:
            residual = inputs

        # skip connection
        x = layers.Add()([x, residual])
        return layers.Activation(self.activation, name=f"{self.name}_{self.activation}2")(x)


def get_resnet18(
    seed=42,
    n_classes=1000,
    activation="relu",
    input_shape=(224, 224, 3),
):
    x_inputs = Input(shape=input_shape, name="input")

    # stage 1
    x = layers.Conv2D(
        64,
        7,
        strides=2,
        name="conv1",
        padding="same",
        kernel_initializer=initializers.HeUniform(seed=seed),
    )(x_inputs)
    x = layers.BatchNormalization(name="bn1")(x)
    x = layers.Activation(activation, name="activation1")(x)
    x = layers.MaxPooling2D(3, strides=2, name="pool1", padding="same")(x)

    # stage 2
    x = ResidualBlock(64, seed=seed, name="conv2_1", activation=activation)(x)
    x = ResidualBlock(64, seed=seed, name="conv2_2", activation=activation)(x)

    # stage 3
    x = ResidualBlock(128, seed=seed, name="conv3_1", activation=activation, projection=True)(x)
    x = ResidualBlock(128, seed=seed, name="conv3_2", activation=activation)(x)

    # stage 4
    x = ResidualBlock(256, seed=seed, name="conv4_1", activation=activation, projection=True)(x)
    x = ResidualBlock(256, seed=seed, name="conv4_2", activation=activation)(x)

    # stage 5
    x = ResidualBlock(512, seed=seed, name="conv5_1", activation=activation, projection=True)(x)
    x = ResidualBlock(512, seed=seed, name="conv5_2", activation=activation)(x)

    # fully-connected
    x = layers.GlobalAveragePooling2D(name="global_avg_pool")(x)
    x = layers.Dense(
        n_classes,
        name="dense",
        activation="softmax",
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x)

    # model
    return Model(inputs=x_inputs, outputs=x, name="ResNet18")

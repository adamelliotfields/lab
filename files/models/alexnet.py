from keras import Input, Model, layers, initializers


# 2nd, 4th, and 5th convolutional layers plus 1st and 2nd dense layers are initialized to 1
def get_alexnet(seed=42, dropout=0.5, classes=1000, activation="relu", input_shape=(227, 227, 3)):
    x_inputs = Input(shape=input_shape, name="input")

    # convolutional layers
    x = layers.Conv2D(
        96,
        11,
        strides=4,
        name="conv1",
        activation=activation,
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x_inputs)
    x = layers.MaxPool2D(3, strides=2, name="pool1")(x)

    x = layers.Conv2D(
        256,
        5,
        name="conv2",
        padding="same",
        activation=activation,
        bias_initializer=initializers.Ones(),
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x)
    x = layers.MaxPool2D(3, strides=2, name="pool2")(x)

    x = layers.Conv2D(
        384,
        3,
        name="conv3",
        padding="same",
        activation=activation,
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x)
    x = layers.Conv2D(
        384,
        3,
        name="conv4",
        padding="same",
        activation=activation,
        bias_initializer=initializers.Ones(),
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x)
    x = layers.Conv2D(
        256,
        3,
        name="conv5",
        padding="same",
        activation=activation,
        bias_initializer=initializers.Ones(),
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x)
    x = layers.MaxPool2D(3, strides=2, name="pool3")(x)

    # fully-connected layers
    x = layers.Flatten(name="flatten")(x)

    x = layers.Dense(
        4096,
        name="dense1",
        activation=activation,
        bias_initializer=initializers.Ones(),
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x)
    x = layers.Dropout(dropout, seed=seed, name="dropout1")(x)

    x = layers.Dense(
        4096,
        name="dense2",
        activation=activation,
        bias_initializer=initializers.Ones(),
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x)
    x = layers.Dropout(dropout, seed=seed, name="dropout2")(x)

    x = layers.Dense(
        classes,
        name="dense3",
        activation="softmax" if classes > 2 else "sigmoid",
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x)

    # model
    return Model(inputs=x_inputs, outputs=x, name="AlexNet")

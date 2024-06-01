from keras import Input, Model, initializers, layers


# originally the images were 32x32 and the first convolutional layer output 28x28
# using padding "same" to keep the output 28x28
def get_lenet(input_shape=(28, 28, 1), classes=10, activation="tanh", seed=42):
    x_inputs = Input(input_shape)

    # convolutional layers
    x = layers.Conv2D(
        6,
        (5, 5),
        strides=1,
        name="conv1",
        padding="same",
        activation=activation,
        kernel_initializer=initializers.RandomUniform(seed=seed),
    )(x_inputs)
    x = layers.MaxPooling2D(
        (2, 2),
        strides=2,
        name="pool1",
    )(x)
    x = layers.Conv2D(
        16,
        (5, 5),
        strides=1,
        name="conv2",
        activation=activation,
        kernel_initializer=initializers.RandomUniform(seed=seed),
    )(x)
    x = layers.MaxPooling2D(
        (2, 2),
        strides=2,
        name="pool2",
    )(x)
    x = layers.Conv2D(
        120,
        (5, 5),
        strides=1,
        name="conv3",
        activation=activation,
        kernel_initializer=initializers.RandomUniform(seed=seed),
    )(x)

    # fully-connected layers
    x = layers.Flatten(name="flatten")(x)
    x = layers.Dense(
        84,
        name="dense1",
        activation=activation,
        kernel_initializer=initializers.RandomUniform(seed=seed),
    )(x)
    x = layers.Dense(
        classes,
        name="dense2",
        activation="softmax" if classes > 2 else "sigmoid",
        kernel_initializer=initializers.RandomUniform(seed=seed),
    )(x)

    # model
    return Model(inputs=x_inputs, outputs=x, name="LeNet5")

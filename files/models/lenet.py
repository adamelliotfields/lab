import keras


# input: 28x28x1
# conv1: 6@28x28, kernel: 5x5, stride: 1, padding: same (6 feature maps of 28x28)
# pool1: 6@14x14, kernel: 2x2, stride: 2
# conv2: 16@10x10, kernel: 5x5, stride: 1
# pool2: 16@5x5, kernel: 2x2, stride: 2
# conv3: 120@1x1, kernel: 5x5, stride: 1
# dense4: 84
# output: 10
def make_lenet(n_classes=10, activation="tanh", optimizer="sgd"):
    inputs = keras.Input((28, 28, 1))

    x = keras.layers.Conv2D(
        6,
        (5, 5),
        strides=1,
        padding="same",
        activation=activation,
    )(inputs)
    x = keras.layers.MaxPooling2D(
        (2, 2),
        strides=2,
    )(x)
    x = keras.layers.Conv2D(
        16,
        (5, 5),
        strides=1,
        activation=activation,
    )(x)
    x = keras.layers.MaxPooling2D(
        (2, 2),
        strides=2,
    )(x)
    x = keras.layers.Conv2D(
        120,
        (5, 5),
        strides=1,
        activation=activation,
    )(x)
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(
        84,
        activation=activation,
    )(x)

    outputs = keras.layers.Dense(
        n_classes,
        activation="softmax" if n_classes > 2 else "sigmoid",
    )(x)

    model = keras.Model(inputs=inputs, outputs=outputs)
    model.compile(
        optimizer=optimizer,
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model

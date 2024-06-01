# The Visual Geometry Group at Oxford University is a renowned research group in computer vision.
# One notable contribution is the VGG model, introduced in the paper, "Very Deep Convolutional
# Networks for Large-Scale Image Recognition" (Simonyan and Zisserman, 2014). At ILSVRC-2014, the
# VGG models achieved a top-5 error rate of 7.3%, narrowly losing to GoogLeNet's 6.7%.
from keras import Input, Model, initializers, layers

CONFIGS = {
    "vgg16": [2, 2, 3, 3, 3],
    "vgg19": [2, 2, 4, 4, 4],
}


def get_vgg(config="vgg16", n_classes=1000, input_shape=(224, 224, 3), activation="relu", seed=42):
    config = config.lower()
    if config not in CONFIGS:
        raise ValueError(f"'{config}' is not available; use one of {list(CONFIGS.keys())}")

    filters = [64, 128, 256, 512, 512]

    x_inputs = Input(shape=input_shape, name="input")
    x = x_inputs

    # convolutional layers
    for stage, n_convs in enumerate(CONFIGS[config]):
        for conv in range(n_convs):
            x = layers.Conv2D(
                filters[stage],
                3,
                padding="same",
                activation=activation,
                name=f"conv{stage+1}_{conv+1}",  # conv1_1, conv1_2, etc
                kernel_initializer=initializers.HeUniform(seed=seed),
            )(x)
        x = layers.MaxPooling2D(2, strides=2, name=f"pool{stage+1}")(x)

    # fully-connected layers
    x = layers.Flatten(name="flatten")(x)
    x = layers.Dense(
        4096,
        name="dense1",
        activation=activation,
        kernel_initializer=initializers.HeUniform(seed=seed),
    )(x)
    x = layers.Dense(
        4096,
        name="dense2",
        activation=activation,
        kernel_initializer=initializers.HeUniform(seed=seed),
    )(x)
    x = layers.Dense(
        n_classes,
        name="dense3",
        activation="softmax" if n_classes > 1 else "sigmoid",
        kernel_initializer=initializers.RandomNormal(mean=0, stddev=0.01, seed=seed),
    )(x)

    # model
    return Model(inputs=x_inputs, outputs=x, name=config.capitalize())

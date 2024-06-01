# Darknet-19 is the backbone for YOLO v2 and was introduced in "YOLO9000: Better, Faster, Stronger"
# (Redmon et al., 2016). It has 19 convolutional layers and 5 max-pooling layers. It has fewer
# parameters than VGG-16 but achieved higher top-5 accuracy on ImageNet. It was trained on the
# standard ImageNet-1000 dataset for 160 epochs using SGD with an initial learning rate of 0.1,
# polynomial learning rate decay with power of 4, weight decay of 0.0005, and momentum of 0.9.
# Random crops, rotations, and color shifts were used for augmentation. After pre-training on
# 224x224 images, it was fine-tuned on 448x448 images with an initial learning rate of 0.001 for 10 epochs.
from keras import Input, Model, initializers, layers


def get_darknet19(
    seed=42,
    dropout=0.0,  # added for additional regularization
    classes=1000,
    activation="relu",
    input_shape=(224, 224, 3),
):
    x_inputs = Input(shape=input_shape, name="input")

    # stage 1
    x = layers.Conv2D(
        32,
        3,
        name="conv1",
        padding="same",
        activation=activation,
        kernel_initializer=initializers.HeUniform(seed=seed),
    )(x_inputs)
    x = layers.MaxPool2D(2, strides=2, name="pool1")(x)

    # stage 2
    x = layers.Conv2D(
        64,
        3,
        name="conv2",
        padding="same",
        activation=activation,
        kernel_initializer=initializers.HeUniform(seed=seed),
    )(x)
    x = layers.MaxPool2D(2, strides=2, name="pool2")(x)

    # stage 3
    for i in range(3):
        x = layers.Conv2D(
            128 if i % 2 == 0 else 64,
            3 if i % 2 == 0 else 1,
            padding="same",
            name=f"conv{i+3}",
            activation=activation,
            kernel_initializer=initializers.HeUniform(seed=seed),
        )(x)
    x = layers.MaxPool2D(2, strides=2, name="pool3")(x)

    # stage 4
    for i in range(3):
        x = layers.Conv2D(
            256 if i % 2 == 0 else 128,
            3 if i % 2 == 0 else 1,
            padding="same",
            name=f"conv{i+6}",
            activation=activation,
            kernel_initializer=initializers.HeUniform(seed=seed),
        )(x)
    x = layers.MaxPool2D(2, strides=2, name="pool4")(x)

    # stage 5
    for i in range(5):
        x = layers.Conv2D(
            512 if i % 2 == 0 else 256,
            3 if i % 2 == 0 else 1,
            padding="same",
            name=f"conv{i+9}",
            activation=activation,
            kernel_initializer=initializers.HeUniform(seed=seed),
        )(x)
    x = layers.MaxPool2D(2, strides=2, name="pool5")(x)

    # stage 6
    for i in range(5):
        x = layers.Conv2D(
            1024 if i % 2 == 0 else 512,
            3 if i % 2 == 0 else 1,
            padding="same",
            name=f"conv{i+14}",
            activation=activation,
            kernel_initializer=initializers.HeUniform(seed=seed),
        )(x)
    x = layers.Dropout(dropout, seed=seed, name="dropout")(x)

    # output
    x = layers.Conv2D(
        classes,
        1,
        name="conv19",
        padding="same",
        activation=None,
        kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=0.01, seed=seed),
    )(x)
    x = layers.GlobalAveragePooling2D(name="avgpool")(x)
    x = layers.Activation("softmax" if classes > 1 else "sigmoid", name="activation")(x)

    return Model(inputs=x_inputs, outputs=x, name="Darknet19")

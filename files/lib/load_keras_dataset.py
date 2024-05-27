import tensorflow as tf

from keras import datasets


# fetches a Keras dataset and returns a TensorFlow Dataset
# since these are just Numpy matrices, you need to get the column names externally
def load_keras_dataset(
    name: str,
    map_func=None,
    batch_size=0,
    shuffle=False,
    shuffle_buffer_size=0,
    as_numpy=False,
    test_split=0.2,
    seed=42,
):
    if name == "mnist":
        (X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()
    elif name == "cifar10":
        (X_train, y_train), (X_test, y_test) = datasets.cifar10.load_data()
    elif name == "cifar100":
        (X_train, y_train), (X_test, y_test) = datasets.cifar100.load_data(
            label_mode="fine",
        )
    elif name == "imdb":
        (X_train, y_train), (X_test, y_test) = datasets.imdb.load_data(
            seed=seed,
        )
    elif name == "reuters":
        (X_train, y_train), (X_test, y_test) = datasets.reuters.load_data(
            test_split=test_split,
            seed=seed,
        )
    elif name == "fashion_mnist":
        (X_train, y_train), (X_test, y_test) = datasets.fashion_mnist.load_data()
    elif name == "california_housing":
        (X_train, y_train), (X_test, y_test) = datasets.california_housing.load_data(
            version="large",
            test_split=test_split,
            seed=seed,
        )
    else:
        raise ValueError(f"Unknown Keras dataset: {name}")

    if as_numpy:
        return (X_train, y_train), (X_test, y_test)

    # https://www.tensorflow.org/api_docs/python/tf/data/Dataset
    ds_train = tf.data.Dataset.from_tensor_slices((X_train, y_train))
    ds_test = tf.data.Dataset.from_tensor_slices((X_test, y_test))

    if shuffle:
        ds_train = ds_train.shuffle(
            seed=seed,
            buffer_size=ds_train.cardinality()
            if shuffle_buffer_size == 0
            else shuffle_buffer_size,
        )

    if map_func is not None:
        ds_train = ds_train.map(map_func, num_parallel_calls=tf.data.AUTOTUNE)
        ds_test = ds_test.map(map_func, num_parallel_calls=tf.data.AUTOTUNE)

    if batch_size > 0:
        ds_train = ds_train.batch(batch_size)
        ds_test = ds_test.batch(batch_size)

    ds_train = ds_train.prefetch(buffer_size=tf.data.AUTOTUNE)
    ds_test = ds_test.prefetch(buffer_size=tf.data.AUTOTUNE)

    return ds_train, ds_test

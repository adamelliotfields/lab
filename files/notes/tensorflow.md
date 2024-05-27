# TensorFlow

Notes on the inner workings of TensorFlow.

## Tensors

Tensors are like NumPy arrays in that they are n-dimensional with a uniform dtype.

Unlike NumPy arrays, they are immutable. In other words:

```py
tensor = tf.constant([1, 2, 3])
tensor[0] = 4  # will raise an error
```

If you need a mutable tensor, you can use `Variable`. In neural networks, the weights and biases are stored as `Variable` tensors.

Tensors, like matrices, have a _rank_. A scalar has rank 0, a vector has rank 1, a matrix has rank 2, and so on. A tensor does not have to be array-like. You can create a scalar tensor with `tf.constant(42)`.

The _shape_ of a tensor is the length of each axes. For instance, a shape of `(3, 2)` means the tensor has 3 rows and 2 columns. The _size_ is the total number of elements in the tensor, which is the product of the shape values (in this case, 6).

Note that you do not have to manually manage tensors in memory as they get freed when out of scope. However, if you're using TensorFlow.js, you must call `tensor.dispose()` or wrap your code in a `tf.tidy()` callback.

### Ragged Tensors

A tensor is _ragged_ if it has a variable number of elements along some axis. For instance, a tensor with shape `(3, None)` has 3 rows, but the number of elements in each row is not fixed. This cannot be represented as a regular tensor, so use `tf.ragged.constant` to create a `RaggedTensor`:

```py
ragged_tensor = tf.ragged.constant([
    [1, 2],
    [3, 4, 5],
    [6],
])
```

### Sparse Tensors

To store sparse data efficiently:

```py
sparse_tensor = tf.sparse.SparseTensor(
    indices=[[0, 0], [1, 2]],
    values=[1, 2],
    dense_shape=[3, 4],
)
```

This creates a 3x4 tensor with the values 1 and 2 at the specified indices.

## Automatic Differentiation

To differentiate automatically, TensorFlow needs to keep track of what operations happen during the forward pass and then traverse that list in reverse order to compute the gradients during the backward pass.

The `GradientTape` API is provided for gradient computation. Within the context of a `GradientTape`, TensorFlow keeps track of all operations on `Variable` objects. After the forward pass, you can call `tape.gradient(target, sources)` to compute the gradients of the target tensor with respect to the source tensors. The target is usually a loss and the sources are the model's trainable weights.

Constant `Tensor`s are not watched by default. You must call `tape.watch(my_tensor)` on them. If you want a `Variable` tensor to be _ignored_, you can use the `trainable=False` keyword argument.

## Execution Graphs

Normally your TensorFlow code is eager, meaning operations are executed immediately. Ideally, you want to use _graph execution_. In a graph, the nodes are operations and the edges are tensors (the data that flows through the nodes). Converting your code to a graph allows it to be parallelized and even run on devices that don't have Python (the graph is just a data structure).

In TensorFlow, you can create a graph using `tf.function` as a wrapper or decorator. It returns a `PolymorphicFunction`, which is a special type that builds a graph from a Python function. `tf.function` applies to the function it decorates as well as the functions called within it. It is _polymorphic_ because it actually creates multiple graphs from a single function; if a new set of inputs (arguments) can't be handled by an existing graph, it creates a new one.

TensorFlow functions are written using a combination of Python operators like `if`, `break`, and `return` with TensorFlow `tf.*` operations.

## Modules

A _model_ can be distilled down to a function that computes something on tensors during the forward pass, and a variable (weights) that can be updated in response to training.

Models are composed of _layers_, which are the fundamental building blocks of neural networks. For example, a dense layer performs a linear transformation (matrix multiplication) followed by an activation function; a convolutional layer applies a convolution operation to the input data.

In TensorFlow, layers inherit from the `Module` parent class. Typically you would use a library like Keras (included with TensorFlow) or Sonnet (Deepmind) rather than implementing common layers from scratch.

Here's what the `Dense` layer and a `Sequential` model look like:

```py
class Dense(tf.Module):
    def __init__(self, in_units, out_units, name=None):
        super().__init__(name=name)
        w_init = tf.random.normal([in_units, out_units])
        b_init = tf.zeros([out_units])
        self.w = tf.Variable(w_init, name="w")
        self.b = tf.Variable(b_init, name="b")
    def __call__(self, x):
        y = tf.matmul(x, self.w) + self.b
        return y


class SequentialModel(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.dense_1 = Dense(in_units=4, out_units=16)
        self.dense_2 = Dense(in_units=16, out_units=3)
    def __call__(self, x):
        x = self.dense_1(x)
        x = tf.nn.relu(x)
        x = self.dense_2(x)
        x = tf.nn.softmax(x)
        return x


model = SequentialModel(name="my_model")
```

## Distributed Training

TensorFlow allows you to train on multi-GPU machines and even clusters of them with the `tf.distribute` API. By default, it will use all available GPUs.

Anything that contains TensorFlow variables must be called in a `MirroredStrategy` context. For multi-machine clusters, there is also a `MultiWorkerMirroredStrategy`. In this context, all variables and graphs are replicated across devices. Each variable is a type of _distributed variable_ known as a _mirrored variable_.

```py
strategy = tf.distribute.MirroredStrategy()

# everything up to the `compile` call goes in here
with strategy.scope():
    model = get_compiled_model()

# everything else is normal
model.fit(X_train, y_train, epochs=10)
model.evaluate(X_test, y_test)
```

## Transfer Learning

_Transfer learning_ is taking weights learned to solve one problem and using them to solve a different but related problem. A trivial example would be using weights learned to classify cats and dogs as a starting point to learn how to classify tigers and lions.

A typical transfer learning workflow involves instantiating a base model and loading the pre-trained weights into it. Keras provides a bunch of built-in model architectures you can start with, like Xception. You can set `weights="imagenet"` to automatically load the weights from a model trained on ImageNet; or you can provide a path to weights you've already saved or downloaded.

Then you need to freeze the base model by setting `model.trainable = False` and add a new, smaller model on top of it. You'll set `training=False` when you pass the inputs to the frozen model so it runs in inference mode and doesn't update the weights. The output of the base model is then passed to the new model.

### Fine-tuning

Once the model has converged on the new dataset, you can unfreeze the base model and retrain the whole thing using a smaller learning rate, which can lead to further improvements.

## Resources

* https://www.tensorflow.org/guide/tensor
* https://www.tensorflow.org/guide/autodiff
* https://www.tensorflow.org/guide/intro_to_graphs
* https://www.tensorflow.org/guide/intro_to_modules
* https://www.tensorflow.org/js/guide/tensors_operations#memory
* https://www.tensorflow.org/tutorials/distribute/custom_training
* https://keras.io/guides/distributed_training_with_tensorflow
* https://keras.io/guides/transfer_learning

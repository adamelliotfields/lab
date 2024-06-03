# Convolutional Neural Networks (CNN)

[Convolutional neural networks](https://en.wikipedia.org/wiki/Convolutional_neural_network) are a class of deep neural networks most commonly associated with the field of computer vision.

Traditional feed-forward neural networks are not optimized for high-dimensional data like images and audio. For example, a small 100x100x3 color image would result in a 30,000-dimension input vector when flattened. This is larger than most word embeddings (the input to large language models like GPT).

## Image Data

Images are represented as matrices of pixel values. For instance, a grayscale image is a 2D array where each pixel can have 256 possible values or shades (0-255). Color images typically use three channels (RGB) combining to form _24-bit color depth_ with over 16 million colors ($2^{24}$). This can be thought of as stacking three 2D arrays to form a full-color image.

## Convolutions

A [convolution](https://en.wikipedia.org/wiki/Convolution) is a mathematical operation that combines two functions to produce a third function. This derived function expresses how the shape of one function is modified by the other. In the context of CNNs, the convolution operation is used to extract features from an input image. It does this using a _filter_ or _kernel_, which is a small matrix of numbers.

![Convolution animation](../assets/convolution.gif)

> Source: [Google](https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks)

## Filters

The filter "slides" over the input image and computes the dot product of the filter matrix and the image region it covers. The dot products are combined and passed to an activation function like ReLU. Each result is a single element in a new 2D array called a _feature map_ or _convolved feature matrix_. You can think of each color channel in the original image as an individual feature map.

The depth of the filter matches the number of input feature maps. Since the the input image has 3 color channels, the shape of the filters in the first convolutional layer will be $H \times W \times 3$.

Each convolutional layer has multiple filters. If you have 32 filters in your first layer, you will end up with 32 feature maps. Each feature map represents a different feature detected by the filter.

Each filter is initialized randomly (or with Glorot/He) and optimized using gradient descent. Because each filter starts with a different "seed", they learn to detect different features over time.

The size of the feature map is determined by how much the filter moves in each step, known as _stride_. The stride size is usually 1, but can be larger to reduce the size of the feature map. With a stride of 1, a 3x3 filter will produce a 98x98 feature map from a 100x100 image. If you have 32 filters, then you'll end up with a 98x98x32 tensor.

For a convolutional layer, the output size can be calculated using:

$\text{Output Size} = \lfloor \frac{\text{Input Size} - \text{Filter Size} + 2 \times \text{Padding}}{\text{Stride}} \rfloor + 1$

Similarly, for a pooling layer:

$\text{Output Size} = \lfloor \frac{\text{Input Size} - \text{Filter Size}}{\text{Stride}} \rfloor + 1$

> NB: The $\lfloor$ and $\rfloor$ symbols denote the floor function, which rounds a real number down to the nearest integer.

## Pooling

Pooling layers reduce the spatial dimensions (height and width) of the feature maps. The most common type of pooling is _max pooling_. A 2x2 max pooling operation reduces the dimensions of the feature map by half. This helps in reducing the computational load and the complexity of the model.

Max pooling extracts the most "activated" pixels from the feature map and reduces their spatial dimensions. This process is also known as _downsampling_. This helps the model focus on the most important features which allows it to generalize better (reduces overfitting). This means the network can recognize features regardless of their exact position or size in images.

![Max pooling animation](../assets/max-pooling.gif)

> Source: [Google](https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks)

## Receptive Field

A typical CNN is a stack of convolutional and pooling layers followed by a flattening layer and a fully-connected (dense) neural network. Because the output of the pooling layer is high-dimensional, it must be flattened to 1D (a vector) before being passed to the dense input layer.

The filters in each convolutional layer have a _receptive field_, which is the "patch" of the feature map they are able to see. In the first layer, the receptive field is the size of the filter multiplied by the stride. Subsequent layers take into account the receptive field of the previous layer. The formula is:

$$
R_{n} = R_{n-1} + (F - 1) \times S
$$

Where $R_{n}$ is the receptive field of layer $n$, $R_{n-1}$ is the receptive field of the previous layer, $F$ is the size of the filter, and $S$ is the stride. As the network deepends, the receptive field grows to be a larger portion of the input image. For example, if the filters are 3x3 with a stride of 1, by the third layer the receptive field is 7x7 or a 49-pixel square of the original image.

## Padding

Previously I mentioned that a 100x100 image with a filter size of 3x3 and a stride of 1 would result in a 98x98 feature map. This reduction in size is known as the _border effect_ and it means that the edges of the image are not fully captured by the filter. It occurs because the filter "hangs off" the edge of the image when convolving the outer pixels.

To mitigate the border effect, _padding_ is used to add extra pixels around the input image, typically with a value of 0. This ensures that the filter can fully cover the image and the output feature map has the same dimensions as the input image. The formula for calculating the output size of the feature map is:

$$
O = \frac{W - F + 2P}{S} + 1
$$

Where $O$ is the output size, $W$ is the input size (width), $F$ is the filter size, $P$ is the padding, and $S$ is the stride.

In Keras, you can add padding to a convolutional layer with the `padding` keyword argument. The two options are `valid` (no padding) and `same` (padding with zeros). When using `padding="same"` with `strides=1`, the output size will be the same as the input size.

## Output Layer

Like with all neural networks, the output layer and activation function depend on the task. If you are classifying the digits 0-9 (multiclass), then your output layer would have 10 neurons and use softmax activation. If you were doing binary classification or multilabel classification, you would use sigmoid activation.

## AlexNet

Introduced by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton in [2012](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf), AlexNet was the winning entry in the [ImageNet](https://arxiv.org/abs/1409.0575v3) Large Scale Visual Recognition Challenge that year (ILSVRC2012).

### ImageNet

The ImageNet dataset was created by Fei-Fei Li and her team at Stanford. At the time, the dataset contained over 10 million images and 10,000 classes. For the competition, the training set contained 1.2 million images across 1000 classes. The test set contained 150,000 images.

### Training

They trained using SGD with a batch size of 128, momentum of 0.9, and weight decay of 0.0005. Weights were initialized with a Gaussian distribution with a mean of 0 and standard deviation of 0.01. Biases in the 2nd, 4th, and 5th convolutional layers plus both dense layers were initialized to 1; all other biases were initialized to 0.

The learning rate was adjusted manually. When they observed the loss not improving (plateauing), they divided the learning rate by 10 (now `ReduceLROnPlateau` in Keras).

They trained for 90 epochs over 6 days (2x GTX 580 3GB). Starting with a learning rate of 0.01, they reduced it 3 times during training.

### Reducing overfitting

Data augmentation was used to reduce overfitting. They started by taking random 224x224 patches of the original 256x256 images and then making horizontal flips of the patches. Note that to make a prediction, they would make 5 patches of the input image and another 5 flipped patches and average the network's predictions made on each patch.

The second augmentation technique was to alter the intensities of the RGB channels. They performed PCA on the RGB values of the entire ImageNet training set and used the principal components (directions of maximum variance) and eigenvalues (magnitude of variance) to perturb the RGB channels of the training images. These perturbations simulate different lighting conditions.

They found that 50% dropout was necessary to reduce overfitting as well, but doubled the number of epochs necessary to converge.

Finally, no regularization layers (e.g., L1, L2) were used at all.

### Model architecture

* Input: 224x224x3
* Convolution w/ 11x11 kernel +2 pad +4 stride (ReLU): 55x55x96
* Max pooling w/ 3x3 kernel +2 stride: 27x27x96
* Convolution w/ 5x5 kernel +2 pad +1 stride (ReLU): 27x27x256
* Max pooling w/ 3x3 kernel +2 stride: 13x13x256
* Convolution w/ 3x3 kernel +1 pad +1 stride (ReLU): 13x13x384
* Convolution w/ 3x3 kernel +1 pad +1 stride (ReLU): 13x13x384
* Convolution w/ 3x3 kernel +1 pad +1 stride (ReLU): 13x13x256
* Max pooling w/ 3x3 kernel +2 stride: 6x6x256
* Flatten: 9216
* Dense (ReLU, 50% dropout): 4096
* Dense (ReLU, 50% dropout): 4096
* Output (Softmax): 1000

## Resources

### Videos

https://www.youtube.com/watch?v=KuXjwB4LzSA

https://www.youtube.com/watch?v=HGwBXDKFk9I

https://www.youtube.com/watch?v=pj9-rr1wDhM

https://www.youtube.com/watch?v=jDe5BAsT2-Y

### Posts

https://colah.github.io/posts/2014-07-Conv-Nets-Modular/

https://colah.github.io/posts/2014-07-Understanding-Convolutions/

https://developer.ibm.com/articles/introduction-to-convolutional-neural-networks/

https://mathworld.wolfram.com/Convolution.html

https://www.codecademy.com/learn/dlsp-classification-track/modules/dlsp-image-classification/cheatsheet

https://www.freecodecamp.org/news/an-intuitive-guide-to-convolutional-neural-networks-260c2de0a050/

http://yann.lecun.com/exdb/lenet/

### Projects

https://adamharley.com/nn_vis/cnn/3d.html

https://github.com/lutzroeder/netron

https://cs.stanford.edu/people/karpathy/convnetjs/

https://github.com/vdumoulin/conv_arithmetic

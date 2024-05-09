# Deep Learning [WIP]

> Deep learning allows computational models that are composed of multiple processing layers to learn representations of data with multiple levels of abstraction. These methods have dramatically improved the state-of-the-art in speech rec-ognition, visual object recognition, object detection and many other domains such as drug discovery and genomics. Deep learning discovers intricate structure in large data sets by using the backpropagation algorithm to indicate how a machine should change its internal parameters that are used to compute the representation in each layer from the representation in the previous layer. Deep convolutional nets have brought about breakthroughs in processing images, video, speech and audio, whereas recurrent nets have shone light on sequential data such as text and speech. - [LeCun et al., 2015](https://hal.science/hal-04206682/document)

## Early work

* [Perceptron](https://websites.umass.edu/brain-wars/files/2016/03/rosenblatt-1957.pdf) (Rosenblatt, 1958)
  - A single-layer, feed-forward network with a threshold activation function.
  - Unable to solve non-linearly separable problems like XOR.
* [Neocognitron](https://www.rctn.org/bruno/public/papers/Fukushima1980.pdf) (Fukoshima, 1980)
  - Multiple convolutional and pooling (downsampling) layers.
  - Inspired by Hubel and Wiesel's research on the visual cortex.
* [Backpropagation](https://www.cs.utoronto.ca/~hinton/absps/naturebp.pdf) (Rumelhart et al., 1986)
  - Weights are adjusted by propagating errors backwards through the network.
* [CNN with backpropagation](https://proceedings.neurips.cc/paper_files/paper/1989/file/53c3bce66e43be4f209556518c2fcb54-Paper.pdf) (LeCun et al., 1989)
  - All weights learned by backpropagation (previous networks had fixed weights in the first layers).
  - Training 30 epochs took 3 days on a Sun SPARCstation 1 (like an 80's Nvidia DGX).
* [LSTM](https://www.bioinf.jku.at/publications/older/2604.pdf) (Hochreiter and Schmidhuber, 1997)
  - Long Short-Term Memory networks, designed to avoid the vanishing and exploding gradient problems in RNNs.
  - Introduced more complex memory cell units with input and output gates.
* [MNIST](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf) (LeCun et al., 1998)
  - Modified NIST database of handwritten digits (60k train, 10k test).
  - Introduced LeNet-4 and LeNet-5 model architectures.
  - Distorting training images shown to improve accuracy.
  - Demonstrated boosting by combining 3 LeNet-4 models each trained differently.
  - Training 20 epochs took 3 days on a SGI Origin 2000 with a 200MHz R10000 CPU.
* [Deep Belief Networks](https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf) (Hinton et al., 2006)
  - Stacked Restricted Boltzmann Machines (RBMs) trained with unsupervised learning.
  - Demonstrated pre-training each layer to find good initial weights.
* [AlexNet](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) (Krizhevsky et al., 2012)
  - Trained on subset of ImageNet, a dataset of 15M images in 22k categories.
  - Subset included 1.2M training images, 150k testing images, and 50k validation images across 1k categories.
  - Used ReLU activation, normalization and dropout layers, image augmentation, and stochastic gradient descent with momentum and weight decay to improve training efficiency and reduce overfitting.
  - Used distributed training on 2 Nvidia GTX 580 3GB GPUs, which took 6 days.
  - Final model had 60M parameters and 650k neurons.
* [ResNet](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf) (He et al., 2016)
  - Research by Microsoft on very deep networks using residual or "skip" connections.
  - See this [post](https://torch.ch/blog/2016/02/04/resnets.html) and [repo](https://github.com/facebookarchive/fb.resnet.torch) for the original Torch (Lua) implementation.
* [Deep Learning](https://hal.science/hal-04206682/document) (LeCun et al., 2015)
  - Review of deep learning methods and applications.

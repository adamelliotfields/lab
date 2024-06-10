<div align="center">
  <img src="./jupyter.jpg" width="270" alt="Jupyter over a cosmic data lake" />
  <h1><code>lab</code></h1>
  <a href="https://github.com/codespaces/new/adamelliotfields/lab?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json">
    <img src="https://img.shields.io/badge/launch-codespace-24292E?logo=github" alt="Launch Codespace" />
  </a>
</div>
<br />

This is my central repository for machine learning and AI research and experiments.

Each notebook has links to [Colab](https://colab.research.google.com), [Kaggle](https://www.kaggle.com) and [Nbviewer](https://nbviewer.org); if they can run in Pyodide then they also have a link to my [JupyterLite](https://lab.aef.me/lab/).

## Notebooks

- [**Autograd**](./files/autograd.ipynb): "From scratch" [iris](https://www.rdocumentation.org/packages/datasets/topics/iris) classifier neural network with [Autograd](https://github.com/HIPS/autograd).
- [**California Housing**](./files/california_housing.ipynb): EDA and regression with the [California Housing](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html) dataset.
- [**Draw**](./files/draw.ipynb): Drawing app made with [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) and [ipycanvas](https://github.com/jupyter-widgets-contrib/ipycanvas).
- [**EDA**](./files/eda.ipynb): Notes and snippets for exploratory data analysis.
- [**Functions**](./files/functions.ipynb): Explanations and illustrations of activations, loss functions, and optimization algorithms.
- [**Monash**](./files/monash.ipynb): Exploring some of [Monash](https://forecastingdata.org)'s datasets on [🤗](https://huggingface.co/datasets/monash_tsf).
- [**Plotly**](./files/plotly.ipynb): [PX](https://plotly.com/python/plotly-express/) examples.
- [**Profiling**](./files/profiling.ipynb): Demo of [Ydata-profiling](https://github.com/ydataai/ydata-profiling) FKA Pandas Profiling
- [**Sklearn**](./files/sklearn.ipynb): A walkthrough of [Scikit-learn](https://github.com/scikit-learn/scikit-learn).
- [**Sktime**](./files/sktime.ipynb): Forecasting [sunspots](https://www.rdocumentation.org/packages/datasets/topics/sunspots) with models from [Sktime](https://github.com/sktime/sktime).
- [**Statsmodels**](./files/statsmodels.ipynb): Visualizing various datasets included with [Statsmodels](https://github.com/statsmodels/statsmodels).
- [**Sympy**](./files/sympy.ipynb): Plotting algebraic functions with [SymPy](https://www.sympy.org/en/index.html).
- [**W&B**](./files/wandb.ipynb): Experiment tracking and artifact logging on [Weights & Biases](https://wandb.ai).
- [**Widgets**](./files/widgets.ipynb): Interactive widget examples with [ipywidgets](https://github.com/jupyter-widgets/ipywidgets).
- [**Yellowbrick**](./files/yellowbrick.ipynb): Visualizing a Random Forest classifier with [Yellowbrick](https://github.com/DistrictDataLabs/yellowbrick).

### TensorFlow

- [**Autoencoder**](./files/tf/autoencoder.ipynb): Denoising convolutional autoencoder for [MNIST](http://yann.lecun.com/exdb/mnist/).
- [**CIFAR**](./files/tf/cifar.ipynb): Fine-tuning image classifiers on the [CIFAR](https://www.cs.toronto.edu/~kriz/cifar.html) datasets.
- [**KerasCV**](./files/tf/keras_cv.ipynb): Visualize advanced image augmentations from [KerasCV](https://keras.io/keras_cv/).
- [**MNIST**](./files/tf/mnist.ipynb): Predict handwritten digits including an ipywidgets demo.
- [**RNN**](./files/tf/rnn.ipynb): Time series forecasting and sentiment analysis with RNNs, LSTMs, and GRUs.
- [**Shakespeare**](./files/tf/shakespeare.ipynb): Multilayer LSTM trained on [Shakespeare](https://cs.stanford.edu/people/karpathy/char-rnn/) for character prediction.
- [**TensorBoard**](./files/tf/tensorboard.ipynb): Watch your tensors flow with TensorBoard and [Keras Tuner](https://keras.io/keras_tuner/).
- [**XOR**](./files/tf/xor.ipynb): Exclusive OR classifier including an ipywidgets demo.

### PyTorch

- [**Iris**](./files/torch/iris.ipynb): Iris classifier with [Lighting](https://github.com/Lightning-AI/pytorch-lightning) for training.
- [**NeuralProphet**](./files/neuralprophet.ipynb): Demonstration of forecasting [airline passengers](https://www.rdocumentation.org/packages/datasets/topics/AirPassengers) with [NeuralProphet](https://github.com/ourownstory/neural_prophet).

## Models

> Keras [functional](https://keras.io/guides/functional_api/) implementations from papers.

- [**AlexNet**](./files/models/alexnet.py): [ImageNet Classification with Deep Convolutional Neural Networks](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) (Krizhevsky et al., 2012)
- [**Darknet-19**](./files/models/darknet19.py): [YOLO9000: Better, Faster, Stronger](https://arxiv.org/abs/1612.08242) (Redmon and Farhadi, 2016)
- [**LeNet-5**](./files/models/lenet.py): [Gradient-Based Learning Applied to Document Recognition](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf) (LeCun et al., 1998)
- [**ResNet-18**](./files/models/resnet18.py): [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) (He et al., 2015)
- [**SqueezeNet**](./files/models/squeezenet.py): [AlexNet-level Accuracy with 50x Fewer Parameters](https://arxiv.org/abs/1602.07360) (Iandola et al., 2016)
- [**VGG-16/19**](./files/models/vgg.py): [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556) (Simonyan and Zisserman, 2014)

## Apps

### Gradio

- [**Iris**](./files/gradio/iris.py): Iris classifier and data visualizer with API.
- [**Todos**](./files/gradio/todos.py): Todo app demonstrating session state and custom CSS.

## Installation

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# graphviz
sudo apt install -y graphviz

# ta-lib
wget https://github.com/TA-Lib/ta-lib/releases/download/v0.4.0/ta-lib-0.4.0-src.tar.gz
tar -xvf ta-lib-0.4.0-src.tar.gz
cd ta-lib
./configure --prefix=/usr
make
sudo make install
```

## Usage

To run the JupyterLab server on port [8888](http://localhost:8888):

```sh
make
```

To run the JupyterLite server on port [8000](http://localhost:8000):

```sh
make lite
```

See [`Makefile`](./Makefile) for more scripts.

## Environment

```sh
HF_TOKEN=hf...
WANDB_API_KEY=abc...
```

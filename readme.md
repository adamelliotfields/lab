<div align="center">
  <img src="./jupyter.jpg" width="270" alt="Jupyter over a cosmic data lake" />
  <h1><code>lab</code></h1>
  <a href="https://github.com/codespaces/new/adamelliotfields/lab?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json">
    <img src="https://img.shields.io/badge/launch-codespace-24292E?logo=github" alt="Launch Codespace" />
  </a>
</div>
<br />

This is my central repository for all my machine learning and AI research and experiments.

Each notebook has links to [Colab](https://colab.research.google.com), [Kaggle](https://www.kaggle.com) and [Nbviewer](https://nbviewer.org); if they can run in Pyodide then they also have a link to my [JupyterLite](https://lab.aef.me/lab/).

## Notebooks

- [**Autograd**](./files/autograd.ipynb): "From scratch" [iris](https://www.rdocumentation.org/packages/datasets/topics/iris) classifier neural network with [Autograd](https://github.com/HIPS/autograd).
- [**Draw**](./files/draw.ipynb): Drawing app made with [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) and [ipycanvas](https://github.com/jupyter-widgets-contrib/ipycanvas).
- [**EDA**](./files/eda.ipynb): Notes and snippets for exploratory data analysis.
- [**Functions**](./files/functions.ipynb): Explanations and illustrations of activations, loss functions, and optimization algorithms.
- [**Monash**](./files/monash.ipynb): Exploring some of [Monash](https://forecastingdata.org)'s datasets on [🤗](https://huggingface.co/datasets/monash_tsf).
- [**NeuralProphet**](./files/neuralprophet.ipynb): Demonstration of forecasting [airline passengers](https://www.rdocumentation.org/packages/datasets/topics/AirPassengers) with [NeuralProphet](https://github.com/ourownstory/neural_prophet).
- [**Plotly**](./files/plotly.ipynb): [PX](https://plotly.com/python/plotly-express/) examples.
- [**Profiling**](./files/profiling.ipynb): Demo of [Ydata-profiling](https://github.com/ydataai/ydata-profiling) FKA Pandas Profiling
- [**Sklearn**](./files/sklearn.ipynb): A walkthrough of [Scikit-learn](https://github.com/scikit-learn/scikit-learn).
- [**Sktime**](./files/sktime.ipynb): Forecasting [sunspots](https://www.rdocumentation.org/packages/datasets/topics/sunspots) with models from [Sktime](https://github.com/sktime/sktime).
- [**Statsmodels**](./files/statsmodels.ipynb): Visualizing various datasets included with [Statsmodels](https://github.com/statsmodels/statsmodels).
- [**Sympy**](./files/sympy.ipynb): Plotting algebraic functions with [SymPy](https://www.sympy.org/en/index.html).
- [**Widgets**](./files/widgets.ipynb): Interactive widget examples with [ipywidgets](https://github.com/jupyter-widgets/ipywidgets).
- [**Yellowbrick**](./files/yellowbrick.ipynb): Visualizing a Random Forest classifier with [Yellowbrick](https://github.com/DistrictDataLabs/yellowbrick).

### TensorFlow

- [**KerasCV**](./files/tf/keras_cv.ipynb): Visualize advanced image augmentations from [KerasCV](https://keras.io/keras_cv/).
- [**MNIST**](./files/tf/mnist.ipynb): Predict handwritten digits including an ipywidgets demo.
- [**TensorBoard**](./files/tf/tensorboard.ipynb): Watch your tensors flow with TensorBoard and [Keras Tuner](https://keras.io/keras_tuner/).
- [**XOR**](./files/tf/xor.ipynb): Exclusive OR classifier including an ipywidgets demo.

### PyTorch

- [**Iris**](./files/torch/iris.ipynb): Iris classifier with [Lighting](https://github.com/Lightning-AI/pytorch-lightning) for training.

### Datasets

- [**Diabetes**](./files/data/diabetes.ipynb): Original unscaled version from [2003](https://hastie.su.domains/Papers/LARS/LeastAngle_2002.pdf).
- [**Hatch**](./files/data/hatch.ipynb): 18,000+ UFO sightings from 593 BCE to 2003 CE.
- [**SPY**](./files/data/spy.ipynb): SPY and VXX 1-minute OHLCV data from 2020 for forecasting.
- [**USPS**](./files/data/usps.ipynb): Digit classification dataset from [1989](http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf).

## Models

> Keras [functional](https://keras.io/guides/functional_api/) models.

- [**LeNet**](./files/models/lenet.py): [LeNet-5](https://en.wikipedia.org/wiki/LeNet) implementation for [MNIST](https://en.wikipedia.org/wiki/MNIST_database).
- [**SqueezeNet**](./files/models/squeezenet.py): [SqueezeNet](https://arxiv.org/abs/1602.07360) with residual connections.

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

Notebooks that interact with Hugging Face (like downloading a dataset) require an API token in your environment. Create a `.env` file with:

```sh
HF_TOKEN=hf...
```

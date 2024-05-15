<div align="center">
  <img src="./jupyter.jpg" width="270" alt="Jupyter over a cosmic data lake" />
  <h1><code>lab</code></h1>
  <a href="https://github.com/codespaces/new/adamelliotfields/lab?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json">
    <img src="https://img.shields.io/badge/launch-codespace-24292E?logo=github" alt="Launch Codespace" />
  </a>
</div>
<br />

Notebooks and [lab.aef.me](https://lab.aef.me).

## Notebooks

- [Autograd](./files/autograd.ipynb): "From scratch" [iris](https://www.rdocumentation.org/packages/datasets/topics/iris) classifier neural network with [Autograd](https://github.com/HIPS/autograd).
- [Draw](./files/draw.ipynb): Drawing app made with [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) and [ipycanvas](https://github.com/jupyter-widgets-contrib/ipycanvas).
- [EDA](./files/eda.ipynb): Snippets and notes on exploratory data analysis.
- [Monash](./files/monash.ipynb): Exploring some of [Monash](https://forecastingdata.org)'s datasets on [🤗](https://huggingface.co/datasets/monash_tsf).
- [NeuralProphet](./files/neuralprophet.ipynb): Demonstration of forecasting [airline passengers](https://www.rdocumentation.org/packages/datasets/topics/AirPassengers) with [NeuralProphet](https://github.com/ourownstory/neural_prophet).
- [Plotly](./files/plotly.ipynb): [PX](https://plotly.com/python/plotly-express/) examples.
- [Profiling](./files/profiling.ipynb): Demo of [Ydata-profiling](https://github.com/ydataai/ydata-profiling) FKA Pandas Profiling
- [Sklearn](./files/sklearn.ipynb): A walkthrough of [Scikit-learn](https://github.com/scikit-learn/scikit-learn).
- [Sktime](./files/sktime.ipynb): Forecasting [sunspots](https://www.rdocumentation.org/packages/datasets/topics/sunspots) with models from [Sktime](https://github.com/sktime/sktime).
- [Statsmodels](./files/statsmodels.ipynb): Visualizing various datasets included with [Statsmodels](https://github.com/statsmodels/statsmodels).
- [Sympy](./files/sympy.ipynb): Plotting algebraic functions with [SymPy](https://www.sympy.org/en/index.html).
- [Widgets](./files/widgets.ipynb): Interactive widget examples with [Ipywidgets](https://github.com/jupyter-widgets/ipywidgets).
- [Yellowbrick](./files/yellowbrick.ipynb): Visualizing a Random Forest classifier with [Yellowbrick](https://github.com/DistrictDataLabs/yellowbrick).

### PyTorch

- [Iris](./files/torch/iris.ipynb): Iris classifier with [Lighting](https://github.com/Lightning-AI/pytorch-lightning) for training.

### TensorFlow

- [XOR](./files/tf/xor.ipynb): XOR classifier.

### Datasets

- [Diabetes](./files/data/diabetes.ipynb): Original unscaled version from [2003](https://hastie.su.domains/Papers/LARS/LeastAngle_2002.pdf).
- [Hatch](./files/data/hatch.ipynb): 18,000+ UFO sightings from 593 BCE to 2003 CE.
- [SPY-VXX](./files/data/spy_vxx.ipynb): SPY and VXX 1-minute OHLCV data for 2020.
- [USPS](./files/data/usps.ipynb): Digit classification dataset from [1989](http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf).

## Installation

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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

## Environment

Create a `.env` file with:

```sh
HF_TOKEN=hf...
```

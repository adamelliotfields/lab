<div align="center">
  <img src="./jupyter.jpg" width="270" alt="Jupyter over a cosmic data lake" />
  <h1><code>lab</code></h1>
  <a href="https://github.com/codespaces/new/adamelliotfields/lab?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json">
    <img src="https://img.shields.io/badge/launch-codespace-24292E?logo=github" alt="Launch Codespace" />
  </a>
</div>
<br />

[Notebooks](./files) and [aef.me/lab](https://aef.me/lab/).

## Installation

### Pip

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Conda

```sh
conda env create -f environment.yml
conda activate lab
```

## Usage

To run the JupyterLab server on [:8888](http://localhost:8888):

```sh
make
```

To run the JupyterLite server on [:8000](http://localhost:8000):

```sh
make lite
```

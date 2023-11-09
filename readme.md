<div align="center">
  <img src="./jupyter.jpg" width="270" alt="Jupyter over a cosmic data lake" />
  <h1><code>jupyter</code></h1>
  <a href="https://github.com/codespaces/new/adamelliotfields/jupyter?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json">
    <img src="https://img.shields.io/badge/launch-codespace-24292E?logo=github" alt="Launch Codespace" />
  </a>
  <a href="https://mybinder.org/v2/gh/adamelliotfields/jupyter/main">
    <img src="https://mybinder.org/badge_logo.svg" alt="Launch Binder" />
  </a>
</div>
<br />

Notes on running JupyterLab and writing notebooks.

## Usage

See [`Makefile`](./Makefile).

```bash
python -m venv venv
venv/bin/pip install -r requirements.txt
```

## Notes

[Jupyter Notebook](https://jupyter-notebook.readthedocs.io) was originally the web interface for IPython. After a few years, it was [split](https://blog.jupyter.org/the-big-split-9d7b88a031a7) into a separate project. The name is a loose combination of JUlia, PYThon, and R, as it now polyglot.

> [!NOTE]
> I use "notebook" to refer to the file format and "Notebook" to refer to the application.

[JupyterLab](https://jupyterlab.readthedocs.io) is the next-gen web IDE for notebooks. The backend runs on Tornado and communicates with kernels (runtimes) over ZeroMQ.

[JupyterLite](https://jupyterlite.readthedocs.io) is JupyterLab running entirely in the browser. It uses [Pyodide](https://pyodide.org), which is CPython ported to WebAssembly via Emscripten. Because everything is running in Web Workers in the browser, you can run JS notebooks as well. You can use the version hosted in the docs [here](https://jupyterlite.readthedocs.io/en/stable/_static/lab/index.html).

[Jupyter Console](https://jupyter-console.readthedocs.io) is a terminal-based REPL for Jupyter kernels (IPython by default).

### Desktop

There is an official Electron-based [desktop app](https://github.com/jupyterlab/jupyterlab-desktop).

JetBrains includes [DataSpell](https://www.jetbrains.com/dataspell) in their all-products subscription. It has database support and GitHub Copilot.

For mobile, there's [Juno](https://juno.sh).

For GPU acceleration on macOS, PyTorch has support for Metal now and Apple provides a [plugin](https://developer.apple.com/metal/tensorflow-plugin) for TensorFlow.

### Cloud

#### [Kaggle](https://www.kaggle.com)

Kaggle is totally free. Each week you get 30 hours of GPU time and 20 hours of TPU time. You can also store up to 100GB of datasets.

#### [Google Colab](https://colab.research.google.com)

Colab is also free, but based on platform availability. For $10/mo you get access to Google's Code LLM, Codey, and 100 compute units. For $50/mo you get 500 compute units and your notebooks can execute in the background for up to 24hrs. Beyond the plans, additonal packs of 100 units are $10 each.

Compute units are a combination of CPU, GPU/TPU, and RAM. The base VM is 2 vCPU and 12GB RAM and uses 0.08 units/hr. For 0.12 units/hr you get 8 vCPU and 48GB RAM. A TPU or T4 is ~2 units/hr, and a V100 is ~5 units/hr.

Colab is part of Google Drive, so your notebooks are always in the cloud and your notebooks can read other files from your Drive. You can even connect Colab to a local Jupyter server or Docker container. Every notebook already has a ton of packages installed so you can start coding immediately.

#### [Paperspace](https://www.paperspace.com/notebooks)

The free plan is limited to public notebooks only. For $8/mo you get access to better hardware and private notebooks, and $35/mo gives you access to even better GPUs.

Each plan has different free VMs available on a first-come, first-serve basis. If all of the allocated VMs are being used, you have to wait in line. This applies to CPU-only VMs as well.

If there are no free VMs available and you don't want to wait, you can pay-per-hour. CPU-only machines are only a few cents and you can scale up to 8x A100s for $25/hr.

Paperspace is now part of Digital Ocean, so they also offer a private container registry and model endpoint hosting. You can deploy your trained models to production on the same platform.

#### [JetBrains DataLore](https://www.jetbrains.com/datalore)

Looks like DataSpell in the cloud for $20/mo. Seems like it would make sense for companies using other JetBrains cloud services like Spaces and YouTrack.

#### [Binder](https://mybinder.org)

A free public service sponsored by OVH Cloud and the GESIS-Leibniz Institute that converts a public Git repo to a Docker container and runs it in the cloud. It uses [`repo2docker`](https://github.com/jupyterhub/repo2docker) under the hood to build the container. No account necessary. Click [here](https://mybinder.org/v2/gh/fastai/numerical-linear-algebra/master) to run the [fast.ai Computational Linear Algebra](https://www.fast.ai/posts/2017-07-17-num-lin-alg.html) course on Binder.

#### [nbviewer](https://nbviewer.org)

A web application for rendering notebooks hosted on GitHub. [Here](https://nbviewer.org/github/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/01-g-h-filter.ipynb) is the first chapter of the [Kalman and Bayesian Filters](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python) book by Roger Labbe.

### VS Code

When opening a notebook for the first time you'll need to [pick the Jupyter kernel](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management) to use.

If you do not get IntelliSense, then you have to <kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>P</kbd> `Reload Window`.

#### Server

If you want to connect to a running Jupyter server instead of a local runtime, you have to add the `token` query parameter to the URL.

```
http://localhost:8888?token=''
```

#### Linting and Formatting

The [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension (which is included with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension) works out-of-the-box. You can enable type-checking by setting `python.analysis.typeCheckingMode` to **basic** or **strict**.

I'd like to add [Ruff](https://github.com/astral-sh/ruff) when it works in notebooks (waiting for astral-sh/ruff-vscode#256 and astral-sh/ruff-lsp#264 to be released).

[Black](https://github.com/psf/black) formatter works (see [`settings.json`](./.vscode/settings.json)).

### Devcontainers

GitHub has an "Open in JupyterLab" button that will run the JupyterLab server automatically. This works if your devcontainer has `jupyter` installed.

The default devcontainer used by Codespaces is the [`universal`](https://github.com/devcontainers/images/tree/main/src/universal) image, which has a complete machine learning stack (with Jupyter) pre-installed. It also includes Node.

The [`python`](https://github.com/devcontainers/images/tree/main/src/python) image is more for building Python packages or apps. It includes dev tools, but no data science-y stuff (no Jupyter). It comes with NVM, but Node is not pre-installed.

### AI

#### [`jupyter-ai`](https://jupyter-ai.readthedocs.io/en/latest/users/index.html)

Adds a chat widget to JupyterLab that can use different LLM APIs. Also adds an `%ai` magic so you can interact with LLMs from within notebook cells.

It also includes slash commands powered by LangChain. For example, the `/generate` command will request an entire notebook to be built for you. The `/learn` command will embed a folder of files into a local vector database for [RAG](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/).

#### [`pandasai`](https://github.com/gventuri/pandas-ai)

Sends a sample of your data to the OpenAI API to give the LLM context and then generates and runs the code. It can even send faulty generated code back for troubleshooting.

```py
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from sklearn.datasets import load_iris

iris = load_iris()
llm = OpenAI(api_token="your_token")
sdf = SmartDataframe(iris, config={'llm': llm})

sdf.chat('Scatter plot sepal length vs width.')
```

#### [`jupytercoder`](https://github.com/bigcode-project/jupytercoder)

This is a Chrome extension from BigCode (HuggingFace + ServiceNow) that uses the [StarCoder](https://huggingface.co/blog/starcoder) LLM to autocomplete in JupyterLab like GitHub Copilot.

### Interactivity

You can render websites as HTML strings using IPython's `HTML` class:

```py
from IPython.display import HTML
display(HTML('<p style="margin: 0">Hello, world!</p>'))
```

Or with the `%%html` magic:

```html
%%html
<div id="root"></div>
<script src="https://unpkg.com/react@17/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"></script>
<script>
    const e = React.createElement
    const root = document.querySelector('#root')
    const onClick = () => alert('Hola!')
    const Button = () => e('button', { onClick }, 'Click me!')
    const App = () => (
        e(React.Fragment, null,
            e('div', { style: { margin: '0 0 4px' } }, '⚛️'),
            e(Button)
        )
    )
    ReactDOM.render(e(App), root)
</script>
```

But for more complex interactivity, you'll want to use a widget library. The most popular is [`ipywidgets`](https://github.com/jupyter-widgets/ipywidgets). You can even render your interactive notebook as a web app using [`voila`](https://github.com/voila-dashboards/voila).

### Git

Notebooks are just JSON files but they aren't meant to be human-readable. Running a notebook in different applications will change the metadata. This can be messy if you are a `git add .` person.

For viewing diffs, use [`nbdime`](https://github.com/jupyter/nbdime). It can also aid with merging notebooks if you need it. For interacting with Git inside Jupyter, install the [`jupyterlab-git`](https://github.com/jupyterlab/jupyterlab-git) extension.

If you prefer to store your notebooks in Markdown for clean diffs, use [`jupytext`](https://github.com/mwouts/jupytext) for 2-way conversion between `.ipynb` and `.md`.

```sh
pipx install jupytext
jupytext --from=md:markdown --to=ipynb --opt=split_at_heading=true notebook.md
jupytext --from=ipynb --to=md:markdown notebook.ipynb
```

### PDF

You need to install `pandoc` and `basictex` to export to PDF.

> [!WARNING]
> Don't install `mactex` unless you're sure (it's 5GB).

```sh
brew install pandoc
brew install --cask basictex
```

You'll have to exit your terminal to get the Tex binaries in your PATH. You don't need to change your RC files and you shouldn't need to logout/restart. Since `basictex` is a minimal distribution, you'll have to install some additional packages:

```sh
# must be run as root
sudo tlmgr update --self
sudo tlmgr install tcolorbox environ pdfcol adjustbox titling enumitem soul rsfs
```

Now you can convert a notebook to a PDF:

```sh
# creates notebooks/your_notebook.pdf with default styling
jupyter nbconvert notebooks/your_notebook.ipynb --to pdf
```

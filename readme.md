# jupyter

[![Launch Codespace](https://img.shields.io/badge/launch-codespace-24292E?logo=github)](https://github.com/codespaces/new/adamelliotfields/jupyter?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json)
[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/adamelliotfields/jupyter/main)

## Usage

See [`Makefile`](./Makefile).

```bash
# this goes in your RC files (~/.bashrc, ~/.zshrc, etc)
export PYDEVD_DISABLE_FILE_VALIDATION=1
export PATH="${HOME}/.local/bin:${PATH}"

# this installs dependencies
make

# this runs the server (optional)
make jupyter
```

## Notes

### Contents
* [Cloning This Repository](#cloning-this-repository)
* [Devcontainers](#devcontainers)
* [AI](#ai)
* [Kaggle](#kaggle)
* [VS Code](#vs-code)
* [Linting](#linting)
* [Language Servers](#language-servers)
* [Kernels](#kernels)
* [Working Directory](#working-directory)
* [Databases](#databases)
* [Exporting PDFs](#exporting-pdfs)

### Cloning This Repository [:top:](#contents)

The name _jupyter_ appears in:
  * [`devcontainer.json`](./.devcontainer/devcontainer.json)
  * [`package-lock.json`](./package-lock.json)
  * [`package.json`](./package.json)
  * [`pyproject.toml`](./pyproject.toml)
  * [`readme.md`](./readme.md)

You probably want to change it to the name of your project.

### Devcontainers [:top:](#contents)

GitHub has an "Open in JupyterLab" button that will run the JupyterLab server automatically. This works if your devcontainer has `jupyter` installed.

The default devcontainer used by Codespaces is the [`universal`](https://github.com/devcontainers/images/tree/main/src/universal) image, which has a complete machine learning stack (with Jupyter) pre-installed. It also includes Node.

The [`python`](https://github.com/devcontainers/images/tree/main/src/python) image is more for building Python packages or apps. It includes dev tools, but no data science-y stuff (no Jupyter). It comes with NVM, but Node is not pre-installed.

Using a virtual environment or an alternative package manager like Pipenv/Poetry means you need to ensure that JupyterLab is running in the same environment. If you use `ipython` from the terminal, then you need to make sure it's running in the same environment as well. For example: `poetry run jupyter lab` and `poetry run ipython`.

I find that for data projects it's easier to use `requirements.txt`. It's supported by [Binder](https://mybinder.org) and it's also how you define dependencies for apps in 🤗 [Spaces](https://huggingface.co/spaces), so it's good for muscle memory. Finally, using the `universal` devcontainer image means your Codespaces start faster, as everything is installed when the image is built.

### AI [:top:](#contents)

I've installed the [`openai`](https://pypi.org/project/openai) and [`jupyter-ai`](https://pypi.org/project/jupyter-ai) packages, so you only need to export `OPENAI_API_KEY` in whatever shell you're using. You'll need to create a [Codespace secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces) as well.

### Kaggle [:top:](#contents)

The [Kaggle CLI](https://www.kaggle.com/docs/api) allows you to easily download datasets. You need to export `KAGGLE_USERNAME` and `KAGGLE_KEY`.

### VS Code [:top:](#contents)

When opening a notebook for the first time you'll need to [pick the Jupyter kernel](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management) to use. If you want to connect to the running Jupyter server, you have to add the `token` query parameter to the URL.

> [!IMPORTANT]
> The empty quotes are required.

```
http://localhost:8888?token=''
```

If you do not get IntelliSense, then you have to <kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>P</kbd> `Reload Window`. You can also try `Python: Clear Cache and Reload Window` which additionally refreshes the available Python interpreters.

### Linting [:top:](#contents)

[Black](https://github.com/psf/black) is installed and I've set `notebook.formatOnSave.enabled` in [`settings.json`](./.vscode/settings.json).

For linting, the [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension (which is included with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension) works out-of-the-box. You can enable type-checking by setting `python.analysis.typeCheckingMode` to **basic** or **strict**.

I'd like to add [Ruff](https://github.com/astral-sh/ruff) when it works in notebooks in VS Code (astral-sh/ruff-vscode#256).

### Language Servers [:top:](#contents)

You can install additional [language servers](https://jupyterlab-lsp.readthedocs.io/en/latest/Language%20Servers.html) via npm. I've included the [Bash language server](https://github.com/bash-lsp/bash-language-server).

Note that they are mostly for the file editor, not notebooks. For notebooks, you probably want [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

### Kernels [:top:](#contents)

Each kernel has its own installation instructions. I've included the [tslab](https://github.com/yunabe/tslab) kernel for TypeScript and [JupySQL](https://github.com/ploomber/jupysql) for SQL. Also check out the [evcxr](https://github.com/evcxr/evcxr) kernel for Rust.

Use the `kernelspec` command to manage kernels:

```sh
jupyter kernelspec list
```

To remove all the kernels:

```sh
jupyter kernelspec remove -y jslab tslab
```

### Working Directory [:top:](#contents)

There are a couple settings that affect how you load data (e.g., `pd.read_csv()`).

In VS Code's [`settings.json`](./.vscode/settings.json), `jupyter.notebookFileRoot` essentially sets the _working directory_ for notebooks, which affects relative paths. It is **not** the same as Jupyter's `--notebook-dir` and `--ServerApp.root_dir` options. The default is `${fileDirname}` (leave it).

### Databases [:top:](#contents)

With JupySQL you can connect to an in-memory SQLite database using `%sql sqlite://` or an in-memory DuckDB database using `%sql duckdb://`. [Read the docs](https://jupysql.ploomber.io) for more.

### Exporting PDFs [:top:](#contents)

You need to install `pandoc` and `basictex`.

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

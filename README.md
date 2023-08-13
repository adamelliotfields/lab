# jupyter-codespace

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/adamelliotfields/jupyter-codespace?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json)

Running JupyterLab in a Codespace. Inspired by [github/codespaces-jupyter](https://github.com/github/codespaces-jupyter).

## Usage

See [`Makefile`](./Makefile).

```bash
# this goes in your dotfiles (probably already there)
export PATH="${HOME}/.local/bin:${PATH}"

# this installs dependencies
make

# this runs the server
make jupyter
```

## Notebooks

Make sure you commit your `*.ipynb` [notebook](./notebooks) files, as GitHub automatically renders them (the generated images are [Data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)).

## Language Servers

You can install additional [language servers](https://jupyterlab-lsp.readthedocs.io/en/latest/Language%20Servers.html) via npm. I've included the [Bash language server](https://github.com/bash-lsp/bash-language-server).

Note that they are mostly for the file editor, not notebooks. For notebooks, you probably want [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

## Kernels

Each kernel has its own installation instructions. I've included the [tslab](https://github.com/yunabe/tslab) kernel for TypeScript and [JupySQL](https://github.com/ploomber/jupysql) for SQL. Also check out the [evcxr](https://github.com/evcxr/evcxr) kernel for Rust.

## Databases

With JupySQL you can connect to an in-memory SQLite database using `%sql sqlite://` or an in-memory DuckDB database using `%sql duckdb://`. [Read the docs](https://jupysql.ploomber.io) for more.

To actually run a database container inside your Codespace, you'll want to use [Docker-in-Docker](https://github.com/devcontainers/features/tree/main/src/docker-in-docker).

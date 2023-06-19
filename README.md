# jupyter-codespace

Running JupyterLab in a Codespace. Inspired by [github/codespaces-jupyter](https://github.com/github/codespaces-jupyter).

## Usage

See [`Makefile`](./Makefile).

```bash
# this goes in your dotfiles (probably already there)
export PATH="${HOME}/.local/bin:${PATH}"

# this installs dependencies (run on devcontainer creation)
make

# this runs the server (optional)
make jupyter
```

## Language Servers

You can install additional [language servers](https://jupyterlab-lsp.readthedocs.io/en/latest/Language%20Servers.html) via npm. I've included the [Bash language server](https://github.com/bash-lsp/bash-language-server).

Note that they are mostly for the file editor, not notebooks. For notebooks, you probably want [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

## Kernels

Each kernel has its own installation instructions. I've included the [tslab](https://github.com/yunabe/tslab) kernel for TypeScript. Also check out the [evcxr](https://github.com/evcxr/evcxr) kernel for Rust.

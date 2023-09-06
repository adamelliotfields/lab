# jupyter-codespace

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/adamelliotfields/jupyter-codespace?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json)

Running JupyterLab in a Codespace. Inspired by [github/codespaces-jupyter](https://github.com/github/codespaces-jupyter) and [DataCamp Workspaces](https://www.datacamp.com/workspace).

## Usage

See [`Makefile`](./Makefile).

```bash
# this goes in your dotfiles (~/.bashrc, ~/.zshrc, etc)
export PYDEVD_DISABLE_FILE_VALIDATION=1
export PATH="${HOME}/.local/bin:${PATH}"

# this installs dependencies
make

# this runs the server (optional)
make jupyter
```

## Notes

### Cloning This Repository

The name _jupyter-codespace_ appears in:
  * [`devcontainer.json`](./.devcontainer/devcontainer.json)
  * [`Makefile`](./Makefile)
  * [`package-lock.json`](./package-lock.json)
  * [`package.json`](./package.json)
  * [`pyproject.toml`](./pyproject.toml)
  * [`readme.md`](./readme.md)

You probably want to change it to the name of your project.

Also, you can change the `universal:2` devcontainer image to `python:3` if you are not using Node. You'll want to remove the `npm` script from the Makefile if you do.

### AI

I've installed the [`openai`](https://pypi.org/project/openai) and [`jupyter-ai`](https://pypi.org/project/jupyter-ai) packages, so you only need to export `OPENAI_API_KEY` in whatever shell you're using. You'll need to create a [Codespace secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces) as well.

### VS Code

When opening a notebook for the first time you'll need to [pick the Jupyter kernel](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management) to use.

The `make` command will create a virtualenv for you via `poetry env use`.

If you want to connect to the running Jupyter server, you have to add the `token` query parameter to the URL.

> [!IMPORTANT]
> The empty quotes are required.

```
http://localhost:8888?token=''
```

If you do not get IntelliSense, then you have to <kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>P</kbd> `Reload Window`. You can also try `Python: Clear Cache and Reload Window` which additionally refreshes the available Python interpreters.

### Linting

[Black](https://github.com/psf/black) is installed and I've set `notebook.formatOnSave.enabled` in [`settings.json`](./.vscode/settings.json).

For linting, the [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension (which is included with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension) works out-of-the-box. You can enable type-checking by setting `python.analysis.typeCheckingMode` to **basic** or **strict**.

I'd like to add [Ruff](https://github.com/astral-sh/ruff) when it works in notebooks in VS Code (it can lint them from the CLI).

### Language Servers

You can install additional [language servers](https://jupyterlab-lsp.readthedocs.io/en/latest/Language%20Servers.html) via npm. I've included the [Bash language server](https://github.com/bash-lsp/bash-language-server).

Note that they are mostly for the file editor, not notebooks. For notebooks, you probably want [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

### Kernels

Each kernel has its own installation instructions. I've included the [tslab](https://github.com/yunabe/tslab) kernel for TypeScript and [JupySQL](https://github.com/ploomber/jupysql) for SQL. Also check out the [evcxr](https://github.com/evcxr/evcxr) kernel for Rust.

Use the `kernelspec` command to manage kernels:

```sh
poetry run jupyter kernelspec list
```

To remove all the kernels:

```sh
poetry run jupyter kernelspec remove -y jupyter-codespace jslab tslab
```

### Databases

With JupySQL you can connect to an in-memory SQLite database using `%sql sqlite://` or an in-memory DuckDB database using `%sql duckdb://`. [Read the docs](https://jupysql.ploomber.io) for more.

To actually run a database container inside your Codespace, you'll want to use [Docker-in-Docker](https://github.com/devcontainers/features/tree/main/src/docker-in-docker).

### Codespace Simple Browser

Codespaces have an embedded [Simple Browser](https://github.blog/changelog/2022-10-20-introducing-the-codespaces-simple-browser)[^1] that can be opened automatically when launching an application. **I'm not able to get it working at the moment.**

> I just wanted to see if this was possible; you _probably_ want to use a full browser tab.

You can open the Simple Browser manually by right-clicking a port and selecting "Preview in editor". To have it open automatically, add this to [`devcontainer.json`](./.devcontainer/devcontainer.json):

```json
"portsAttributes": {
  "8888": {
    "label": "Jupyter",
    "onAutoForward": "openPreview"
  }
}
```

Add this to the `jupyter_opts_codespace` variable in the [`Makefile`](./Makefile)[^2]:

```sh
--ServerApp.tornado_settings="{'headers': {'Content-Security-Policy': \"frame-ancestors https://${CODESPACE_NAME}-8888.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN} 'self' \"}}"
```

[^1]: https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-github-codespaces-clients#troubleshooting-the-simple-browser

[^2]: https://jupyter-server.readthedocs.io/en/latest/operators/public-server.html#embedding-the-notebook-in-another-website

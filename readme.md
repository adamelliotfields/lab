# jupyter-codespace

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/adamelliotfields/jupyter-codespace?machine=basicLinux32gb&devcontainer_path=.devcontainer/devcontainer.json)

Running JupyterLab in a Codespace. Inspired by [github/codespaces-jupyter](https://github.com/github/codespaces-jupyter) and [DataCamp Workspaces](https://www.datacamp.com/workspace).

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

## Notes

### AI

I've installed the [`openai`](https://pypi.org/project/openai) and [`jupyter-ai`](https://pypi.org/project/jupyter-ai) packages, so you only need to export `OPENAI_API_KEY` in whatever shell you're using. You'll need to create a [Codespace secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces) as well.

The environment variable is used for the [%ai magic](./notebooks/ai.ipynb) and is separate from the Jupyternaut AI assistant. For the latter, you simply paste the key into the input field the first time you use Jupyternaut.

### Notebooks

Make sure you commit your `*.ipynb` [notebook](./notebooks) files, as GitHub automatically renders them (the generated images are [Data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)).

### Language Servers

You can install additional [language servers](https://jupyterlab-lsp.readthedocs.io/en/latest/Language%20Servers.html) via npm. I've included the [Bash language server](https://github.com/bash-lsp/bash-language-server).

Note that they are mostly for the file editor, not notebooks. For notebooks, you probably want [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

### Kernels

Each kernel has its own installation instructions. I've included the [tslab](https://github.com/yunabe/tslab) kernel for TypeScript and [JupySQL](https://github.com/ploomber/jupysql) for SQL. Also check out the [evcxr](https://github.com/evcxr/evcxr) kernel for Rust.

### Databases

With JupySQL you can connect to an in-memory SQLite database using `%sql sqlite://` or an in-memory DuckDB database using `%sql duckdb://`. [Read the docs](https://jupysql.ploomber.io) for more.

To actually run a database container inside your Codespace, you'll want to use [Docker-in-Docker](https://github.com/devcontainers/features/tree/main/src/docker-in-docker).

### Browser

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

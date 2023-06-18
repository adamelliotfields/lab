pipenv_path := $(shell command -v pipenv 2>/dev/null)
npm_path := $(shell command -v npm 2>/dev/null)
npx_path := $(shell command -v npx 2>/dev/null)

jupyter_opts := --IdentityProvider.token='' --ServerApp.use_redirect_file=False
jupyter_opts_codespace := --ServerApp.allow_origin='*' --ServerApp.custom_display_url="https://${CODESPACE_NAME}-8888.preview.app.github.dev" --ip=0.0.0.0 --no-browser

.PHONY: all pip npm tslab jupyter

all: pip npm tslab

pip:
ifdef pipenv_path
	@pipenv install
else
	@python -m pip install --user pipenv
	@pipenv install
endif

npm:
ifdef npm_path
	@npm install
else
	$(error npm is not installed)
endif

tslab:
ifdef npx_path
	@npx tslab install --python="$(shell command -v python)" --binary="${PWD}/node_modules/.bin/tslab"
else
	$(error npx is not installed)
endif

jupyter:
ifdef CODESPACE_NAME
	@pipenv run jupyter lab $(jupyter_opts) $(jupyter_opts_codespace)
else
	@pipenv run jupyter lab $(jupyter_opts)
endif

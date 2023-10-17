mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_abs_path := $(subst Makefile,,$(mkfile_path))

build:
	docker build -t example .

jupyter:
	docker run -v $(current_abs_path):/app --name example-app --rm -p 8888:8888 --env-file .env -t example jupyter lab --port=8888 --ip='*' --NotebookApp.token='' --NotebookApp.password='' --no-browser --notebook-dir=/app --allow-root
    
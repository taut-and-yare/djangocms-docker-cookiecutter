DOCKER := $(shell which docker-compose)
NPM := $(shell which npm)
PYTHON := env/bin/python
PIP := env/bin/pip

all: install-node-packages initial-jade2html docker

$(PYTHON):
	virtualenv -p python3 env

$(PIP): $(PYTHON)
	export CC=gcc
	$(PIP) install -r requirements.txt

install-node-packages: ./src/static/package.json
	#install into static dir
	$(NPM) install --prefix ./src/static
	#install for project as a whloe
	$(NPM) install

initial-jade2html: $(PIP) ./compilejade.sh
	$(NPM) run jade2html

docker:
	docker-compose build
	docker-compose run django python ./src/manage.py migrate
	#docker-compose run django python ./manage.py collectstatic --noinput

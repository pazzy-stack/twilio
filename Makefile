.PHONY: clean venv install analysis test test-install docs docs-install

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install . --use-mirrors

test-install: install
	. venv/bin/activate; pip install -r tests/requirements.txt

develop: venv
	. venv/bin/activate; pip install . -e --use-mirrors

analysis:
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E501 tests
	. venv/bin/activate; flake8 --ignore=F401 twilio

test: analysis
	. venv/bin/activate; \
  find tests -type d | xargs nosetests

cover:
	. venv/bin/activate; \
  find tests -type d | xargs nosetests --with-coverage --cover-inclusive --cover-erase --cover-package=twilio

docs-install:
	. venv/bin/activate; pip install -r docs/requirements.txt

docs:
	. venv/bin/activate; cd docs && make html

release: test-install
	. venv/bin/activate; python setup.py sdist upload
	. venv/bin/activate; python setup.py bdist_wheel upload

build: test-install
	. venv/bin/activate; python setup.py sdist
	. venv/bin/activate; python setup.py bdist_wheel

clean:
	rm -rf venv

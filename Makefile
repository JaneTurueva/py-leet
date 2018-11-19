all:
	@echo "make devenv	- Configure dev environment"
	@echo "make build	- Build sdist & bdist_wheel packages"
	@echo "make clean	- Remove files created by distutils & dev modules"
	@echo "make test	- Run tests"
	@echo "make upload	- Upload to the PyPI registry"
	@exit 0

devenv:
	rm -rf env
	virtualenv env -p python3
	env/bin/pip install -Ue '.[develop]'

clean:
	rm -fr *.egg-info .tox dist

build: clean
	env/bin/python setup.py sdist bdist_wheel

test:
	env/bin/tox

upload: build
	env/bin/twine upload dist/*

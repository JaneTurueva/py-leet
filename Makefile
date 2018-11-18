all: test

devenv:
	rm -r env
	virtualenv env -p python3
	env/bin/pip install -Ue '.[develop]'

clean:
	rm -fr *.egg-info .tox dist

build: clean
	env/bin/python setup.py sdist bdist_wheel

test:
	env/bin/tox

upload: sdist
	env/bin/twine upload dist/*
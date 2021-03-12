.PHONY: build
build:	## package project for PyPi
	python setup.py sdist bdist_wheel
	twine check dist/*

.PHONY: pypitest
pypitest:	## upload project to pypi test server
	twine upload --repository testpypi dist/* --skip-existing

.PHONY: upload
upload:	## upload new version to PyPi
	twine upload dist/* --skip-existing

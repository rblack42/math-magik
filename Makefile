.PHONY:	changes
changes:
	git log --oneline --pretty=format:"* %ad: %s" --date=short > CHANGES

.PHONY: docs
docs:
	cd rst && \
	sphinx-build -b html -d _build/doctrees . ../docs

.PHONY: spelling
spelling:
	cd rst && \
	sphinx-build -b spelling -d _build/doctrees . ../docs

.PHONY: linkcheck
linkcheck:
	cd rst && \
	sphinx-build -b linkcheck -vvv -d _build/doctrees . ../docs

.PHONY: test
test:
	python -m pytest
	flake8 tests

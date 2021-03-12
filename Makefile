.PHONY: venv
venv:	.envrc
	direnv allow

.envrc:
	echo 'layout python3' > .envrc

.PHONY: reqs
reqs:
	pip install -r requirements.txt

.PHONY: test
test:
	python -m pytest

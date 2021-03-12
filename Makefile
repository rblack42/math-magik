.PHONY: venv
venv:	.envrc
	direnv allow

.envrc:
	echo 'layout python3' > .envrc

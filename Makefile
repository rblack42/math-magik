.PHONY:	changes
changes:
	git log --oneline --pretty=format:"* %ad: %s" --date=short > CHANGES

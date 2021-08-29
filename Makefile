# math-magik Makefile
PROJECT := math_magik
MK	:= mk

-include $(MK)/help.mk
-include $(MK)/python.mk
-include $(MK)/pypi.mk
-include $(MK)/version.mk
-include $(MK)/sphinx.mk

.PHONY: mass
mass:
	cd mmdesigner && \
		python WeightBalance.py


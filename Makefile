.PHONY: start stop status restart cli tail build run test pip-compile


help:
	@echo ""
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  task1              to run task1"
	@echo "  task2              to run task2"
	@echo "  profile1           to Memory Profiler task1"
	@echo "  profile2           to Memory Profiler task2"
	@echo ""

task2:
	python task2.py
profile2:
	python -m memory_profiler task2.py

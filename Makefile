# Makefile for managin fastapi, testing and linting.

.DEFAULT_GOAL := check

.PHONY: mypy lint check
mypy:
	poetry run mypy pachka_watcher

lint:
	poetry run flake8 .

check:
	$(MAKE) mypy && $(MAKE) lint


.PHONY: help
help:
	@echo Makefile commands:
	@echo  - check         -- Run mypy and flake8
	@echo  - lint          -- Run flake8
	@echo  - mypy          -- Run mypy

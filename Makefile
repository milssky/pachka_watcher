# Makefile for managin fastapi, testing and linting.

.DEFAULT_GOAL := check

.PHONY: check
check:
	poetry run mypy pachka_watcher && poetry run flake8 .


.PHONY: help
help:
	@echo Makefile commands:
	@echo  - check          -- Run mypy and flake8

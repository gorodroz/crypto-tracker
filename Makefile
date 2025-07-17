VENV_NAME := .venv
PYTHON := $(VENV_NAME)\Scripts\python.exe
PIP := $(VENV_NAME)\Scripts\pip.exe
FLAKE8 := $(VENV_NAME)\Scripts\flake8.exe

.PHONY: help install run lint freeze clean

help:
	@echo Available commands:
	@echo make install  - create virtual environment and install dependencies
	@echo make run      - run the application
	@echo make lint     - check code style with flake8
	@echo make freeze   - export dependencies to requirements.txt
	@echo make clean    - remove virtual environment

install:
	python -m venv $(VENV_NAME)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py

lint:
	$(FLAKE8) .

freeze:
	$(PIP) freeze > requirements.txt

clean:
	rmdir /S /Q $(VENV_NAME)
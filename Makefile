# Makefile for Django project in WSL using uv

# Virtual environment and tools
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = uv pip
MANAGE = $(PYTHON) manage.py

# --- Django commands ---

run:
	$(MANAGE) runserver

migrate:
	$(MANAGE) migrate

makemigrations:
	$(MANAGE) makemigrations

shell:
	$(MANAGE) shell

createsuperuser:
	$(MANAGE) createsuperuser

check:
	$(MANAGE) check

collectstatic:
	$(MANAGE) collectstatic --noinput

test:
	$(MANAGE) test

# --- Dependency Management ---

install:
	$(PIP) install -r requirements.txt

freeze:
	$(PIP) freeze > requirements.txt

# --- Initial Setup ---

init:
	uv venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# --- Clean up ---

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

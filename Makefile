MANAGE_PY=$(VIRTUAL_ENV)/bin/python manage.py
PIP=$(VIRTUAL_ENV)/bin/pip

run:
	@$(MANAGE_PY) runserver

shell:
	@$(MANAGE_PY) shell

clean:
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -exec rm -d "{}" \;

migrations:
	@$(MANAGE_PY) makemigrations

migrate:
	@$(MANAGE_PY) migrate

superuser:
	@$(MANAGE_PY) createsuperuser

requirements:
	@$(PIP) -r requirements.txt

install:
	pip install -r requirements.txt

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

set_env_vars:
	@[ -f .env ] && source .env

serve:
	$(MAKE) set_env_vars
	python3 manage.py runserver

.PHONY: set_env_vars

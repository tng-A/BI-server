install:
	pip install -r requirements.txt

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

superuser:
	python manage.py createsuperuser
collectstatic:
	python manage.py collectstatic
set_env_vars:
	@[ -f .env ] && source .env

serve:
	python3 manage.py runserver

.PHONY: set_env_vars

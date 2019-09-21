.PHONY: install
install:
	python3 -m virtualenv -p python3 venv
	venv/bin/pip install -r requirements.txt
	venv/bin/python manage.py makemigrations
	venv/bin/python manage.py migrate
	venv/bin/python manage.py createsuperuser

.PHONY: serve
serve:
	venv/bin/python manage.py runserver

.PHONY: clear
clear:
	rm -f db.sqlite3
	rm -rf venv
	rm -rf media
	rm -rf static
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete
	find . -path "*.pyc" -delete
	find . -path "*/__pycache__" -delete

.PHONY: generate_secret_key
generate_secret_key:
	venv/bin/python myworkshop/utils/secret_key.py
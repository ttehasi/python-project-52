PORT ?= 8000
install:
	uv sync

render-start:
	uv run gunicorn -b 0.0.0.0:$(PORT) task_manager.wsgi

dock-dev-start:
	docker run -it -p 8000:8000 task_manager:latest

migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate
	
run:
	uv run python manage.py runserver

lint:
	uv run ruff check

test:
	uv run python manage.py test

check: lint test

setup:
	pip install uv
	uv sync
	make migrate
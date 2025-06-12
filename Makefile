PORT ?= 8000
install:
	uv sync

render-start:
	uv run gunicorn -b 0.0.0.0:$(PORT) task_manager.wsgi

dock-dev-start:
	docker run -it -p 8000:8000 task_manager:latest
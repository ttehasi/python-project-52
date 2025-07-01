### Hexlet tests and linter status:
[![Actions Status](https://github.com/ttehasi/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ttehasi/python-project-52/actions)
[![Coverage](https://github.com/ttehasi/python-project-52/actions/workflows/my-check.yml/badge.svg)](https://github.com/ttehasi/python-project-52/actions/workflows/my-check.yml)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=ttehasi_python-project-52&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=ttehasi_python-project-52)
[![Code Coverage](https://qlty.sh/badges/79db35e8-a2db-40e4-a4c6-3084c317f74b/test_coverage.svg)](https://qlty.sh/gh/ttehasi/projects/python-project-52)


### [Проект](https://task-manager-tte.onrender.com) на render.com
****
## Менеджер задач
****
##### Менеджер задач — это веб-приложение для управления задачами, разработанное на Python. Оно позволяет пользователям создавать, отслеживать и управлять задачами, назначать исполнителей, добавлять метка и устанавливать статусы.

### Технологии

Данный проект создан с помощью данных инструментов:

|                                                   | Описание                                                                                           |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [Django](https://www.djangoproject.com/)          | "A high-level Python web framework that encourages rapid development and clean, pragmatic design." |
| [Bootstrap 5](https://getbootstrap.com/)          | "A popular CSS framework for building responsive and mobile-first web projects."                   |
| [PostgreSQL](https://www.postgresql.org/)         | "A powerful, open-source relational database management system."                                   |
| [Gunicorn](https://gunicorn.org/)                 | "A WSGI server for Unix, used to deploy Python applications."                                      |
| [Docker](https://www.docker.com/)                 | "A platform for developing, shipping, and running applications in containers."                     |
| [uv](https://docs.astral.sh/uv/)                  | "An extremely fast Python package and project manager, written in Rust"                            |
| [dj-database-url](https://pypi.org/project/dj-database-url/)| "A Django utility that allows you to configure databases using URL-style strings."                 |
| [Rollbar](https://rollbar.com/)                   | "A tool for error monitoring and real-time issue tracking."                                        |
| [ruff](https://docs.astral.sh/ruff/)              | "An extremely fast Python linter and code formatter, written in Rust"                              |
| [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/)              | "Tweak the form field rendering in templates, not in python-level form definitions."                              |

****
### Установка:

#### Для установки проекта вам понадобится:
- Python 3.12
- uv (быстрый пакетный менеджер)
#### Клонируем репозиторий и переходим в дерикторию проекта:
```
git@github.com:ttehasi/python-project-52.git && cd python-project-52
```
#### Переходим в файл .env.example и конфигурируем его

#### Устанавливаем проект:
```
make setup
```
#### Запуск dev-сервера:
```
make run
```
#### Проект будет доступен по адресу http://127.0.0.1:8000
****
#### Запуск продакшн сервера 
```
make render-start
```
#### Проект будет доступен по адресу http://127.0.0.1:8000

****

* После запуска приложения, зарегистрируйтесь и кайфуте)!

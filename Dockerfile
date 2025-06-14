FROM python:3.13.2-slim

RUN apt-get update && apt-get install -yq make

RUN pip install uv

WORKDIR /app

COPY . .

RUN uv sync

CMD ["make", "render-start"]
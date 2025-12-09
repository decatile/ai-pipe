FROM python:3.14-slim

RUN apt update -y && apt upgrade -y && apt install curl -y && adduser app
USER app

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /home/app
COPY pyproject.toml .
COPY uv.lock .

RUN .local/bin/uv sync --no-dev

COPY src src

EXPOSE 8000

CMD [".venv/bin/fastapi", "run", "./src/main.py"]

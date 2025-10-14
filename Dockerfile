# latest at 14.10 => 18.79mB
FROM python:3.9.24-alpine3.22

RUN apk add --no-cache curl

# Установка Poetry
# Official installer way
# last version 2025-09-21
ENV POETRY_VERSION=2.2.1
ENV POETRY_HOME=/opt/poetry

ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache/pypoetry

RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавление Poetry в PATH
ENV PATH="${POETRY_HOME}/bin:${PATH}"

WORKDIR /app

# Копирование файлов Poetry
COPY pyproject.toml /app

# Установка зависимостей
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Используем виртуальное окружение Python
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.12

RUN pip install poetry

WORKDIR /api

COPY ./pyproject.toml /api/pyproject.toml

RUN poetry install --no-root

CMD ["poetry", "run", "python", "server.py"]
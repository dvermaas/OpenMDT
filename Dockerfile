# Adapted from https://github.com/astral-sh/uv-docker-example/blob/a14ebc89e3a5e5b33131284968d8969ae054ed0d/Dockerfile
FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

ARG SECRET_KEY
ARG DATABASE_URL

ENV PATH="/app/.venv/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV SECRET_KEY=$SECRET_KEY
ENV DATABASE_URL=$DATABASE_URL

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

RUN python manage.py collectstatic --noinput

ENTRYPOINT []

CMD ["gunicorn", "--bind", "0.0.0.0:8994", "--workers", "4", "--threads", "2", "DjangoPolls.wsgi"]
FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG SECRET_KEY
ARG DATABASE_URL
ENV SECRET_KEY=$SECRET_KEY
ENV DATABASE_URL=$DATABASE_URL

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install uv && \
    uv pip install --system -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8994", "--workers", "4", "DjangoPolls.wsgi"]
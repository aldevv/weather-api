FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
WORKDIR /src

RUN pip install  pipenv
COPY Pipfile.lock Pipfile ./
RUN pipenv install --system --deploy --ignore-pipfile
RUN pip install gunicorn

COPY . .

# Establish the runtime user (with no password and no sudo)
RUN useradd -m weather
USER weather

CMD ["gunicorn", "--access-logfile", "-",  "--workers", "3", "--bind", "0.0.0.0:8000", "weather.wsgi:application", "--log-level", "debug"]

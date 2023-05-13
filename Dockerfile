FROM python:3.12-rc-slim-bullseye

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential \
      libpq-dev python3-dev \
      && pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY ./requirements.text /app
RUN pip install --no-cache-dir --requirement /app/requirements.text
COPY . /app

EXPOSE 8000

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
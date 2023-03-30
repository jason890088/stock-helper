FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=True
ENV POETRY_VIRTUALENVS_CREATE=False

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wget 


RUN pip3 install poetry
COPY poetry.lock pyproject.toml /usr/src/app/
RUN poetry install

COPY . /usr/src/app

EXPOSE 8000
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]


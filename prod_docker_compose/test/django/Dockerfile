FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY ./prod_docker_compose/test/django/test.txt ./
RUN apt-get update -yq \
    && apt-get install curl gnupg vim nano -yq \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean -y
RUN python -m pip install --upgrade pip && pip install -r test.txt

WORKDIR /sbd_animal

COPY ./sbd_animal /sbd_animal



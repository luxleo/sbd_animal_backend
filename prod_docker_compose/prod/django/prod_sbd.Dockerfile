FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# 실행 context: /django
# Dockerfile 위치: /django/prod_docker_compose/prod/prod_sbd.Dockerfile
COPY ./prod_docker_compose/prod/django/requirements.txt ./
RUN apt-get update -yq \
    && apt-get install vim nano -yq \
    && apt-get clean \
    && python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR ./sbd_animal
COPY ./sbd_animal /sbd_animal
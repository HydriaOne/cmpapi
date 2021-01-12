FROM python:3.9-alpine 
LABEL MAINTAINER Hydria

# Install needed packages. Notes:
#   * bash: so we can access /bin/bash
#   * git: to ease up clones of repos
#   * ca-certificates: for SSL verification during Pip and easy_install
#   * Other tools: nescesary to build the requeriments

ENV PACKAGES="bash \
  git \
  libffi \
  libffi-dev \
  openssl-dev \
  musl \
  build-base \
  ca-certificates"

ADD . /opt/cmpapi
WORKDIR /opt/cmpapi

RUN apk add --no-cache $PACKAGES

# Install and upgrade Pip & Requeriments
RUN easy_install pip \
    && pip install --upgrade pip \
    && pip install -r /opt/cmpapi/requeriments.txt

EXPOSE 80

CMD ["python", "main.py"]

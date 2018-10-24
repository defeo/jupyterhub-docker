FROM ubuntu:bionic

LABEL maintainer="Luca De Feo <https://defeo.lu/>"

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && apt-get install -y --no-install-recommends \
	python3-pip \
	python3-setuptools \
        sagemath \
	sagemath-jupyter \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install tornado==4.5.3 jupyterhub==0.9.4

RUN useradd -m sage
ENV HOME=/home/sage
WORKDIR $HOME
USER sage

CMD ["jupyterhub-singleuser"]

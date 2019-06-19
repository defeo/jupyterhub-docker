FROM ubuntu:bionic

LABEL maintainer="Luca De Feo <https://defeo.lu/>"

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && apt-get install -y --no-install-recommends \
	python3-pip \
	python3-setuptools \
	python3-dev \
	libreadline-dev \
	g++ \
        sagemath \
	sagemath-jupyter \
	pari-gp \
	libpari-dev \
	gap \
	singular \
	libsingular4-dev \
	openjdk-8-jre \
	openjdk-8-jre-headless \
	scilab \
	r-base \
	r-recommended \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install \
    tornado==4.5.3 \
    jupyterhub==0.9.4 \
    jupyterlab \
    pari_jupyter \
    PySingular jupyter_kernel_singular \
    scilab-kernel 
#    jupyter-kernel-gap

# TODO R kernel

RUN useradd -m sage
ENV HOME=/home/sage
WORKDIR $HOME
USER sage

CMD ["jupyterhub-singleuser"]

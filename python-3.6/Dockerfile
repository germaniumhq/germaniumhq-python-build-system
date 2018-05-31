FROM ubuntu:16.04

RUN apt update -y && \
    apt upgrade -y && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt update -y && \
    apt install python python3.6-venv python3.6-dev binutils -y && \
    python3.6 -m ensurepip && \
    pip3.6 install virtualenv

RUN useradd -m germanium && \
    python3.6 -m virtualenv /python && \
    chown -R germanium:germanium /python

ENV PATH="/python/bin:$PATH"

USER germanium



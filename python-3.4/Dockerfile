FROM ubuntu:16.04

RUN apt update -y && \
    apt upgrade -y && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt update -y && \
    apt install python3.4 python3.4-venv -y && \
    python3.4 -m ensurepip && \
    pip3.4 install virtualenv

RUN useradd -m germanium && \
    python3.4 -m virtualenv /python && \
    chown -R germanium:germanium /python

ENV PATH="/python/bin:$PATH"

USER germanium


FROM ubuntu:16.04

RUN apt update -y && \
    apt upgrade -y && \
    apt install python python-pip -y && \
    pip install virtualenv

RUN useradd -m germanium && \
    python -m virtualenv /python && \
    chown -R germanium:germanium /python

USER germanium
ENV PATH="/python/bin:${PATH}"

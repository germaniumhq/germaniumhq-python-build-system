FROM ubuntu:16.04

RUN apt update -y && \
    apt upgrade -y && \
    apt install python3 python3-pip python3-dev binutils -y && \
    pip3 install virtualenv

RUN useradd -m --home-dir /germanium germanium && \
    python3 -m virtualenv /python && \
    chown -R germanium:germanium /python

ENV PATH="/python/bin:$PATH"

USER germanium


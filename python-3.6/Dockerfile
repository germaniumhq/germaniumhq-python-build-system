FROM ubuntu:16.04

RUN apt update -y && \
    apt upgrade -y && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt update -y && \
    apt install -y \
        python \
        python3.6-venv \
        python3.6-dev \
        binutils \
        git \
        build-essential \
        zlib1g-dev && \
    python3.6 -m ensurepip && \
    pip3.6 install virtualenv

RUN useradd -m --home-dir /germanium germanium && \
    python3.6 -m virtualenv /python && \
    chown -R germanium:germanium /python

ENV PATH="/python/bin:$PATH"

USER germanium

#============================================================================
# Install pyinstaller, with no lsb
#============================================================================
ARG PYINSTALLER_TAG=v3.3.1

# Build bootloader for alpine

RUN git clone https://github.com/pyinstaller/pyinstaller.git /tmp/pyinstaller \
    && cd /tmp/pyinstaller \
    && git checkout v3.2.1 \
    && cp -R /tmp/pyinstaller/bootloader /tmp \
    && git checkout $PYINSTALLER_TAG \
    && rm -rf /tmp/pyinstaller/bootloader \
    && mv /tmp/bootloader /tmp/pyinstaller/bootloader \
    && cd /tmp/pyinstaller/bootloader \
    && python ./waf configure --no-lsb all \
    && pip install .. \
    && rm -Rf /tmp/pyinstaller


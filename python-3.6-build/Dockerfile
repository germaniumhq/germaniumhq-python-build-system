FROM germaniumhq/python:3.6

USER root

COPY _gbs /_gbs/

#======================================
# Allow sub-folder GBSs
#======================================

# Must end, and start with slash.
ONBUILD ARG GBS_PREFIX="/"

#======================================
# Install prerequisite software
#======================================
ONBUILD COPY --chown=germanium:germanium ${GBS_PREFIX}_gbs/build/install-software /src${GBS_PREFIX}_gbs/build/install-software
ONBUILD RUN /_gbs/start.sh /src${GBS_PREFIX}_gbs/build/install-software/install-software.sh "INSTALL SOFTWARE" && \
    chown -R germanium:germanium /src

#======================================
# Prepare dependencies for download
#======================================
ONBUILD USER germanium

# build1
ONBUILD COPY --chown=germanium:germanium ${GBS_PREFIX}_gbs/build/prepare-build1 /src${GBS_PREFIX}_gbs/build/prepare-build1
ONBUILD RUN /_gbs/start.sh /src${GBS_PREFIX}_gbs/build/prepare-build1/prepare-build1.sh "PREPARE BUILD 1"

# build2
ONBUILD COPY --chown=germanium:germanium ${GBS_PREFIX}_gbs/build/prepare-build2 /src${GBS_PREFIX}_gbs/build/prepare-build2
ONBUILD RUN /_gbs/start.sh /src${GBS_PREFIX}_gbs/build/prepare-build2/prepare-build2.sh "PREPARE BUILD 2"

# build3
ONBUILD COPY --chown=germanium:germanium ${GBS_PREFIX}_gbs/build/prepare-build3 /src${GBS_PREFIX}_gbs/build/prepare-build3
ONBUILD RUN /_gbs/start.sh /src${GBS_PREFIX}_gbs/build/prepare-build3/prepare-build3.sh "PREPARE BUILD 3"

# sources are copied only after stage 3
ONBUILD COPY --chown=germanium:germanium . /src

#======================================
# Do the actual build.
#======================================
ONBUILD RUN /_gbs/start.sh /src${GBS_PREFIX}_gbs/build/run-build.sh "RUN BUILD"

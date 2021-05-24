FROM ubuntu:latest
# Install directory
ARG INSTALL=/root/install

# Make necessary folders
RUN mkdir $INSTALL

# Start in install directory
WORKDIR $INSTALL

# Install pkgs we'll need
RUN apt-get update && apt-get install -y python3 \
	python3-dev \
	python3-pip \
	python3-venv

# MultiEncoder directory
ARG MULTI=/root/MultiEncoder

# Make MultiEncoder dir
RUN mkdir $MULTI

# Move to MultiEncoder dir
WORKDIR $MULTI

# Copy all files there
COPY . $MULTI
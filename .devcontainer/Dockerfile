# Base image: Ubuntu 22.04
FROM ubuntu:22.04

# Install basic tools
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    python3 \
    python3-pip \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Install Docker CLI
RUN curl -fsSL https://get.docker.com | sh

# Install Bun
RUN curl https://bun.sh/install | bash

# Make Bun globally available
ENV PATH="/root/.bun/bin:${PATH}"

# Set working directory
WORKDIR /workspace

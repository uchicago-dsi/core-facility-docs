# Pull base Docker image
# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-scipy-notebook
FROM jupyter/scipy-notebook:python-3.9

# Create working directory
WORKDIR /app

# Install packages
COPY requirements.txt .
RUN pip install -r requirements.txt
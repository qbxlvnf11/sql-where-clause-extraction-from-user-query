FROM pytorch/pytorch:2.1.2-cuda11.8-cudnn8-devel

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/opt/conda/lib/python3.10/site-packages

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    vim \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work

COPY requirements.txt .

RUN pip install --upgrade pip \
    --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt-get install nano




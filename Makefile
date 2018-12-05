help:
	@cat Makefile

DATA?="data"
GPU?=0
DOCKER_FILE=docker/Dockerfile
DOCKER=GPU=$(GPU) nvidia-docker
BACKEND=tensorflow
PYTHON_VERSION?=3.6
CUDA_VERSION?=9.0
CUDNN_VERSION?=7
TEST=tests/
SRC=$(shell pwd)

build_tf:
	docker pull tensorflow/tensorflow:latest-gpu

build_t2t:
	docker build -t tensor2tensor --build-arg python_version=$(PYTHON_VERSION) --build-arg cuda_version=$(CUDA_VERSION) --build-arg cudnn_version=$(CUDNN_VERSION) -f $(DOCKER_FILE) .

tf: build_tf
	$(DOCKER) run -it --rm -p 8889:8888 -v $(SRC):/notebooks/workspace tensorflow/tensorflow:latest-gpu

t2t: build_t2t
	$(DOCKER) run -it --rm -v $(SRC):/notebooks/workspace tensor2tensor bash

# Specify that no actual files are created from these make commands 
.PHONY: build_tf tf build_t2t t2t

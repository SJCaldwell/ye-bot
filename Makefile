help:
	@cat Makefile

DATA?="data"
GPU?=0
KERAS_DOCKER_FILE=docker/keras_dockerfile
T2T_DOCKER_FILE=docker/t2t_dockerfile
BUILD_CONTEXT=docker
DOCKER=GPU=$(GPU) nvidia-docker
KERAS_BACKEND=tensorflow
PYTHON_VERSION?=3.6
CUDA_VERSION?=9.0
CUDNN_VERSION?=7
TEST=tests/
SRC=$(shell pwd)

build_keras:
	docker build -t keras -f $(KERAS_DOCKER_FILE) $(BUILD_CONTEXT)

build_t2t:
	docker build -t tensor2tensor -f $(T2T_DOCKER_FILE) $(BUILD_CONTEXT)

keras: build_keras
	$(DOCKER) run --rm -it -v $(SRC):/workspace -v $(DATA):/workspace/data/dataset --env KERAS_BACKEND=$(KERAS_BACKEND) keras bash

t2t: build_t2t
	$(DOCKER) run -it --rm -p 8889:8888 -v $(SRC):/notebooks/workspace tensor2tensor

# Specify that no actual files are created from these make commands 
.PHONY: build_keras keras build_t2t t2t

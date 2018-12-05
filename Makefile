help:
	@cat Makefile

DATA?="data"
GPU?=0
T2T_DOCKER_FILE=docker/t2t_dockerfile
CONTEXT=docker
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
	docker build -t tensor2tensor -f $(T2T_DOCKER_FILE) $(CONTEXT)

tf: build_tf
	$(DOCKER) run -it --rm -p 8889:8888 -v $(SRC):/notebooks/workspace tensorflow/tensorflow:latest-gpu

t2t: build_t2t
	$(DOCKER) run -it --rm -p 8889:8888 -v $(SRC):/notebooks/workspace tensor2tensor

# Specify that no actual files are created from these make commands 
.PHONY: build_tf tf build_t2t t2t

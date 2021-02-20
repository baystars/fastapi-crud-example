MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := test

# all targets are phony
.PHONY: $(shell egrep -o ^[a-zA-Z_-]+: $(MAKEFILE_LIST) | sed 's/://')

TEST_ENDPOINT="http://localhost:8000"

ifneq ("$(wildcard ./.env)","")
  include ./.env
endif

pip: ## Install package by pip
	@pip install -r requirements.txt

run: ## Run server
	uvicorn app.main:app --host=0.0.0.0 --port=8000 --reload

test: test-quiet ## Run test

test-quiet: ## Run test quiet
	pytest -s

test-verbose: ## Run test verbose
	pytest -s --verbose

curl: ## Curl get response
	@curl -X GET "${TEST_ENDPOINT}"/users/

help: ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := run

# all targets are phony
.PHONY: $(shell egrep -o ^[a-zA-Z_-]+: $(MAKEFILE_LIST) | sed 's/://')

FLASK_ENV=development

TEST_ENDPOINT="http://localhost:8000/api/v1"

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

get-test-value:
	@$(eval TOKEN := $(shell cat tests/env.json|jq -r '.TEST_JUDGE_TOKEN'))
	@$(eval SECTION := $(shell cat tests/env.json|jq -r '.TEST_SECTION'))

curl-status: get-test-value
	@curl -X GET "${TEST_ENDPOINT}/status/${SECTION}" -H  "accept: application/json" -H  "X-Authentication: ${TOKEN}"

db-insert:
	@cd $(PWD)/scripts && python db.py

deploy: deploy-test-clean-backup ## Deploy application

deploy-mock:
	@fab mock

deploy-test:
	@fab test deploy:backup=True

deploy-stage:
	@fab stage deploy:backup=True

deploy-prod:
	@fab prod deploy:backup=True

deploy-test-clean-backup: ## Deploy on testing environment and clean old backups
	@fab test deploy:backup=True,clean=True

deploy-stage-clean-backup: ## Deploy on staging environment and clean old backups
	@fab stage deploy:backup=True,clean=True

deploy-prod-clean-backup: ## Deploy on production environment and clean old backups
	@fab prod deploy:backup=True,clean=True

help: ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

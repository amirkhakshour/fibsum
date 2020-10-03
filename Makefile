.PHONY: build run test tox install test retest
PYTEST = py.test -v

##################
# Run on docker
##################
docker-build:
	docker-compose build

docker-run:
	docker-compose up -d

docker-test:
	docker-compose run -v $(PWD)/tests:/app/tests:ro app tox -e test

docker-tox:
	docker-compose run -v $(PWD)/tests:/app/tests:ro app tox -e py38

docker-lint:
	docker-compose run app tox -e lint

##################
# Run locally
##################
install:
	poetry shell
	poetry install

test:
	@poetry run $(PYTEST)

retest:
	@poetry run $(PYTEST) --lf

server:
	@poetry run python fibsum/manage.py run

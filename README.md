# Fibonacci Sum Calculation

## Getting Up and Running Locally

you can use docker to run the app on a container or install and run it locally.

### 1- install using docker
#### Prerequisites
- Docker
- Docker Compose
- `.env` file: you can use .env.example file as a template. just rename it to `.env` file. 

#### How to install:
1-1- Build the Stack:
Open a terminal at the project root and run the following for local development:
```bash
$ docker-compose build 

# you can use makefile too:
$ make docker-build
```
1-2- Run the docker-compose:
```bash
$ docker-compose up

# you can use makefile too:
$ make docker-run
```
you can access the API using the following url:
```
# fibsum:
$ curl http://127.0.0.1:8000/api/v1/fibsum/12
$ curl http://127.0.0.1:8000/api/v1/fibsum/{target_value_as_int}

# health check:
$ curl http://127.0.0.1:8000/api/v1/health
```
#### run tests using created docker container:
```bash
# run tests on all supported python versions
$ make docker-test

# run tests only on default python version: python3.8
$ make docker-tox

```

### 2- install locally without docker (BLAZINGLY FAST!)
Installing the app on your local machine, you can run tests and 
test coverage commands directly. 

#### How to install:
2-1: Install poetry:
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
2-2: Installing dependencies:
```bash
make install
```
2-3: Run server:
```bash
make server
```
#### run tests locally using pytest:
- Run test without overage report:
```bash
make test
```


## todo
1. add swagger documentation
2. improve algorithm in regards to memoization of duplicate paths.
<div align="center">

![logo](docs/CWL-Logo-512.png)

[![License](https://img.shields.io/cocoapods/l/AFNetworking?style=flat-square)](LICENSE)

</div>

## Description

FastAPI application for the CWL (Common Workflow Language) specification. It is a lightweight API application to manage and execute CWL workflows with different workflow engines (called runners).

## Features

* It uses [FastAPI](https://fastapi.tiangolo.com/) framework for API development. FastAPI is a modern, highly performant, web framework for building APIs with Python 3.6+.

* The APIs are served with [Gunicorn](https://gunicorn.org/) server with multiple [Uvicorn](https://www.uvicorn.org/) workers. Uvicorn is a lightning-fast "ASGI" server. It runs asynchronous Python web code in a single process.

* Simple reverse-proxying with [Caddy](https://caddyserver.com/docs/).

* OAuth2 (with hashed password and Bearer with JWT) based authentication

* [CORS (Cross Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/) enabled.

* Dockerized using [python:3.9-slim-bullseye](https://github.com/docker-library/python/blob/bb68424de76756a2d3dc817f87b1f8640112461f/3.8/bullseye/Dockerfile) and optimized for size and functionality.

## Quickstart

### Setup

* Clone the repo. On your workspace directory, run:

    ```
    git clone https://github.com/terradue/cwl-fastapi.git
    ```

* Head over to the `cwl-fastapi` directory.

### Run the App in Containers

To run the application using Docker, make sure you've got [Docker](https://www.docker.com/) and [Docker Compose V2](https://docs.docker.com/compose/cli-command/) installed on your system. From the project's root dirctory, run:

```bash
docker compose up -d
```

### Alternatively, Run the App Locally

If you want to run the application locally, without using Docker, then:

* Create a virtual environment in the root directory. Here I'm using Python's built-in venv in a Unix system. Run:

    ```bash
    python3.9 -m venv .venv
    ```

* Activate the environment. Run:

    ```bash
    source .venv/bin/activate
    ```

* Go to the folder created by cookie-cutter (default is **fastapi-nano**).

* Install the dependencies. Run:

    ```bash
    pip install -r requirements.txt && pip install -r requirements-dev.txt
    ```

* Start the application. Run:

    ```bash
    uvicorn app.main:app --port 5000 --reload
    ```

### Check the APIs

* To play around with the APIs, go to the following link on your browser:

    ```
    http://localhost:5000/docs
    ```

* Press the `authorize` button on the right and add *username* and *password*. The APIs use OAuth2 (with hashed password and Bearer with JWT) based authentication. 

## Folder Structure

This shows the folder structure of the default template.

```
cwl-fastapi
├── app                                 # primary application folder
│   ├── apis                            # this houses all the API modules
│   │   ├── runners.py                  # runners API
│   │   └── workflows.py                # workflows API
│   ├── core                            # this is where the configs live
│   │   ├── auth.py                     # authentication
│   │   ├── config.py                   # configuration and settings
│   ├── main.py                         # main file where the fastAPI() class is called
│   ├── routes                          # this is where all the routes live
│   │   └── views.py                    # file containing the endpoints of all APIs
│   └── tests                           # test package
│       ├── __init__.py                 # empty init file to make the tests folder a package
│       ├── test_api.py                 # functional testing the API responses
│       └── test_functions.py           # unit testing the underlying functions
├── Caddyfile                           # simple reverse-proxy with caddy
├── docker-compose.yml                  # docker-compose file
├── Dockerfile                          # dockerfile
├── LICENSE                             # MIT license
├── makefile                            # Makefile to apply Python linters
├── mypy.ini                            # type checking configs
├── pyproject.toml                      # pep-518 compliant config file
├── README.md                           # a basic readme template
├── requrements-dev.in                  # .in file to enlist the top-level dev requirements
├── requirements-dev.txt                # pinned dev dependencies
├── requirements.in                     # .in file to enlist the top-level app dependencies
└── requirements.txt                    # pinned app dependencies
```

## Stack

* [Caddy](https://caddyserver.com/docs/)
* [Docker](https://www.docker.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Gunicorn](https://gunicorn.org/)
* [Httpx](https://www.python-httpx.org/)
* [Pip-tools](https://github.com/jazzband/pip-tools)
* [Pydantic](https://pydantic-docs.helpmanual.io/)
* [Pytest](https://docs.pytest.org/en/latest/)
* [Starlette](https://www.starlette.io/)
* [Uvicorn](https://www.uvicorn.org/)

## Resources

* [Flask divisional folder structure](https://exploreflask.com/en/latest/blueprints.html#divisional)
* [Deploying APIs built with FastAPI](https://fastapi.tiangolo.com/deployment/)
* [Reverse proxying with Caddy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy)


<div align="center">
✨ 🍰 ✨
</div>

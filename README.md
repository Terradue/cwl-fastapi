<div align="center">

![logo](https://user-images.githubusercontent.com/30027932/134270064-baecfbec-b3e7-4cb7-a07e-c11a58526260.png)


[![Mentioned in Awesome <INSERT LIST NAME>](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/mjhea0/awesome-fastapi#boilerplate)
[![License](https://img.shields.io/cocoapods/l/AFNetworking?style=flat-square)](https://github.com/rednafi/think-asyncio/blob/master/LICENSE)
[![Twitter](https://img.shields.io/twitter/follow/rednafi?style=flat-square)](https://twitter.com/rednafi)

</div>

## Description

This is a minimalistic and extensible [FastAPI](https://fastapi.tiangolo.com/) template that incorporates divisional pattern architecture with [divisional folder structure](https://exploreflask.com/en/latest/blueprints.html#divisional). It's suitable for developing small to medium sized API oriented micro-services. The architecture is similar to what you'd get with Flask's [Blueprint](https://exploreflask.com/en/latest/blueprints.html).

## Features

* It uses [FastAPI](https://fastapi.tiangolo.com/) framework for API development. FastAPI is a modern, highly performant, web framework for building APIs with Python 3.6+.

* The APIs are served with [Gunicorn](https://gunicorn.org/) server with multiple [Uvicorn](https://www.uvicorn.org/) workers. Uvicorn is a lightning-fast "ASGI" server. It runs asynchronous Python web code in a single process.

* Simple reverse-proxying with [Caddy](https://caddyserver.com/docs/).

* OAuth2 (with hashed password and Bearer with JWT) based authentication

* [CORS (Cross Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/) enabled.

* Flask inspired divisional folder structure better decoupling and encapsulation. This is suitable for small to medium backend development.

* Dockerized using [python:3.9-slim-bullseye](https://github.com/docker-library/python/blob/bb68424de76756a2d3dc817f87b1f8640112461f/3.8/bullseye/Dockerfile) and optimized for size and functionality.

## Quickstart

### Setup

* Clone the repo. On your workspace directory, run:

    ```
    git clone https://github.com/rednafi/fastapi-nano.git
    ```

* Head over to the `fastapi-nano` directory.

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

    This will take you to an UI like below:

    ![Screenshot from 2020-06-21 22-15-18](https://user-images.githubusercontent.com/30027932/85229723-5b721880-b40d-11ea-8f03-de36c07a3ce5.png)


* Press the `authorize` button on the right and add *username* and *password*. The APIs use OAuth2 (with hashed password and Bearer with JWT) based authentication. In this case, the username and password is `ubuntu` and `debian` respectively.

    ![Screenshot from 2020-06-21 22-18-25](https://user-images.githubusercontent.com/30027932/85229725-5e6d0900-b40d-11ea-9c37-bbee546f84a8.png)

    Clicking the `authorize` button will bring up a screen like this:

    ![Screenshot from 2020-06-21 22-18-59](https://user-images.githubusercontent.com/30027932/85229729-6036cc80-b40d-11ea-877e-7421b927a849.png)



* Then select any of the `api_a` or `api_b` APIs and put an integer in the number box and click the `authorize` button.

    ![Screenshot from 2020-06-21 22-31-19](https://user-images.githubusercontent.com/30027932/85229992-fcad9e80-b40e-11ea-850d-9ca86259d463.png)


* Hitting the API should give a json response with random integers.

    ![Screenshot from 2020-06-21 22-32-28](https://user-images.githubusercontent.com/30027932/85230016-25359880-b40f-11ea-9196-c46fd72a760c.png)


* Also, notice the `curl` section in the above screen shot. You can directly use the highlighted curl command in your terminal. Make sure you've got `jq` installed in your system.

    ```bash
    curl -X GET "http://localhost:5000/api_a/22" \
         -H "accept: application/json" \
         -H "Authorization: Bearer $(curl -X POST "http://localhost:5000/token" \
                            -H "accept: application/x-www-form-urlencoded" \
                            -d "username=ubuntu&password=debian" | jq -r ".access_token")"
    ```

    This should show a response like this:

    ```json
    {
    "seed": 22,
    "random_first": 5,
    "random_second": 13
    }
    ```

* To test the `GET` APIs with Python, you can use a http client library like [httpx](https://www.python-httpx.org/):

    ```python
    import httpx

    with httpx.Client() as client:

        # Collect the API token.
        r = client.post(
            "http://localhost:5000/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"username": "ubuntu", "password": "debian"},
        )
        token = r.json()["access_token"]

        # Use the token value to hit the API.
        r = client.get(
            "http://localhost:5000/api_a/22",
            headers={"Accept": "application/json", "Authorization": f"Bearer {token}"},
        )
        print(r.json())
    ```

## Folder Structure

This shows the folder structure of the default template.

```
fastapi-nano
├── app                                 # primary application folder
│   ├── apis                            # this houses all the API packages
│   │   ├── api_a                       # api_a package
│   │   │   ├── __init__.py             # empty init file to make the api_a folder a package
│   │   │   ├── mainmod.py              # main module of api_a package
│   │   │   └── submod.py               # submodule of api_a package
│   │   └── api_b                       # api_b package
│   │       ├── __init__.py             # empty init file to make the api_b folder a package
│   │       ├── mainmod.py              # main module of api_b package
│   │       └── submod.py               # submodule of api_b package
│   ├── core                            # this is where the configs live
│   │   ├── auth.py                     # authentication with OAuth2
│   │   ├── config.py                   # sample config file
│   │   └── __init__.py                 # empty init file to make the config folder a package
│   ├── __init__.py                     # empty init file to make the app folder a package
│   ├── main.py                         # main file where the fastAPI() class is called
│   ├── routes                          # this is where all the routes live
│   │   └── views.py                    # file containing the endpoints of api_a and api_b
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

In the above structure, `api_a` and `api_b` are the main packages where the code of the APIs live and they are exposed by the endpoints defined in the `routes` folder. Here, `api_a` and `api_b` have identical logic. Basically these are dummy APIs that take an integer as input and return two random integers between zero and the input value. The purpose of including two identical APIs in the template is to demonstrate how you can decouple the logics of multiple APIs and then assemble their endpoints in the routes directory. The following snippets show the logic behind the dummy APIs.

This is a dummy submodule that houses a function called `random_gen` which basically generates a dict of random integers.

```python
# This a dummy module
# This gets called in the module_main.py file
from __future__ import annotations
import random


def rand_gen(num: int) -> dict[str, int]:
    num = int(num)
    d = {
        "seed": num,
        "random_first": random.randint(0, num),
        "random_second": random.randint(0, num),
    }
    return d
```

The `main_func` in the primary module calls the `rand_gen` function from the submodule.

```python
from __future__ import annotations
from app.api_a.submod import rand_gen


def main_func(num: int) -> dict[str, int]:
    d = rand_gen(num)
    return d
```

The endpoint is exposed like this:

```python
# app/routes/views.py
from __future__ import annotations
#... codes regarding authentication ...

# endpoint for api_a (api_b looks identical)
@router.get("/api_a/{num}", tags=["api_a"])
async def view_a(num: int, auth: Depends =Depends(get_current_user)) -> dict[str, int]:
    return main_func_a(num)
```

So hitting the API with a random integer will give you a response like the following:

```json
{
  "seed": 22,
  "random_first": 27,
  "random_second": 20
}
```

## Further Modifications

* You can put your own API logics in the shape of `api_a` and `api_b` packages. You'll have to add additional directories like `api_a` and `api_b` if you need more APIs.

* Then expose the APIs in the `routes/views.py` file. You may choose to create multiple `views` files to organize your endpoints.

* This template uses OAuth2 based authentication and it's easy to change that. FastAPI docs has a comprehensive list of the available [authentication options](https://fastapi.tiangolo.com/tutorial/security/) and instructions on how to use them.

* You can change the application port in the `.env` file.

* During prod deployment, you might need to fiddle with the reverse-proxy rules in the Caddyfile.

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

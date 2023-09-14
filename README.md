# msisdn-app-api
MSISDN App API

## Getting started
Run ```docker build .``` to build the docker image.

Run ```docker-compose build``` to run the above command, but use the docker-compose.yml file.

## Linting

Flake8 was used for linting the code in this project. To run, from the main project directory enter:
```
docker-compose run --rm app sh -c "flake8"
```

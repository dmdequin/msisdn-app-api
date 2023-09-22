# msisdn-app-api
MSISDN App API

Project Description:  Create a Django app that takes an MSISDN (Mobile Station International Subscriber Directory Number) as an input and returns associated information, including:
- MNO (Mobile Network Operator) identifier
- country dialing code
- subscriber number and
- country identifier (ISO 3166-1-alpha-2)


## Project requirements
**Git**:
You will need Git to clone the project repository.

**Docker Desktop**:
Running this project locally requires installation of Docker Desktop.</br>
Since development is all done through Docker, there are no other local installations needed.

I personally used a version of Docker suitable for Ubutu WSL, but the OS should not matter. Versions I installed were:
- Docker v24.0.6
- Docker-compose v2.20.2

## Getting started with local development
Install Git and Docker Desktop.

In the termninal navigate to a place you would like to clone this repository.
Run ```git clone https://github.com/dmdequin/msisdn-app-api.git```
Navigate to the root directory of the project: ```cd msisdn-app-api```

Run ```docker-compose build``` to build the docker image while using the docker-compose.yml file.

## Run Project with Docker
After building the docker image run: ```docker-compose up```
Then go to [http://localhost:8000/api/msisd/home/](http://localhost:8000/api/msisd/home/) to access the MSISD API search home page.

To test admin functionality go to: [http://localhost:8000/admin](http://localhost:8000/admin)
Create a superuser in the terminal by entering ```docker-compose run --rm app sh -c "python manage.py createsuperuser```
Then login to the admin page using the admin credentials you provided.

## Documentation Page
Swagger is used in this project to generate a documentation page for the API. This can be accessed at [http://localhost:8000/api/docs](http://localhost:8000/api/docs). All of the API endpoints are listed, and you are able to test different actions such as POST or GET.

## Linting Locally

Flake8 is used for linting the code in this project. To run code linting, from the main project directory enter:
```
docker-compose run --rm app sh -c "flake8"
```

## Testing Locally
This project contains unit tests that test each of the apps (user and msisd). Automated testing was configured using GitHub Actions. To run the tests locally enter the following from the main project directory:
```
docker-compose run --rm app sh -c "python manage.py test"
```

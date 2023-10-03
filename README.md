# msisdn-app-api
MSISDN App API

Project Description:  Create a Django app that takes an MSISDN (Mobile Station International Subscriber Directory Number) as an input and returns associated information, including:
- MNO (Mobile Network Operator) identifier
- country dialing code
- subscriber number and
- country identifier (ISO 3166-1-alpha-2)

When entering in a number that is not already in the database, the field information is parsed automatically and the entry is added to the database.


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

To build the app in development run ```docker-compose build```. This will build the docker image while using the docker-compose.yml file.

## Run Project with Docker
After building the docker image run: ```docker-compose up```
Then go to [http://localhost:8000/api/msisd/home/](http://localhost:8000/api/msisd/home/) to access the MSISD API search home page.

To test admin functionality go to: [http://localhost:8000/admin](http://localhost:8000/admin)
Create a superuser in the terminal by entering ```docker-compose run --rm app sh -c "python manage.py createsuperuser```
Then login to the admin page using the admin credentials you provided.

## Documentation Page
Swagger is used in this project to generate a documentation page for the API. This can be accessed at [http://localhost:8000/api/docs](http://localhost:8000/api/docs). All of the API endpoints are listed, and you are able to test different actions such as POST or GET.

## Linting and Testing Locally

This project uses Flake8 for linting the code. To run code linting, from the main project directory enter: ```docker-compose run --rm app sh -c "flake8"```

This project contains unit tests that test each of the apps (user and msisd). To run the tests locally enter the following from the main project directory: ```docker-compose run --rm app sh -c "python manage.py test"```.

Automated testing and linting was configured using GitHub Actions. This is completed after each push to the remote repository.

## App in Development

The app in development can be run locally for testing. To do so:
- Go to line 37 in the docker-compose-deploy.yml file and change the port mapping for the proxy to 8000:8000 (it is currently set to 80:8000).
- Enter the proxy directory and run ```docker build .``` to build the docker image there.
- Go back to the main directory and run ```docker-compose -f docker-compose-deploy.yml up``` to run the application.
- In the browser go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and test out the various endpoints.


## Deployed App

The deployed version of this app can be found at [http://ec2-34-239-104-90.compute-1.amazonaws.com/](http://ec2-34-239-104-90.compute-1.amazonaws.com/).

All endpoints can be tested from here. For example, the documentation can be found at [http://ec2-34-239-104-90.compute-1.amazonaws.com/api/docs/](http://ec2-34-239-104-90.compute-1.amazonaws.com/api/docs/).

The frontend search of the API for users can be found at [http://ec2-34-239-104-90.compute-1.amazonaws.com/api/msisd/home/](http://ec2-34-239-104-90.compute-1.amazonaws.com/api/msisd/home/).
# msisdn-app-api
MSISDN App API

Project Description:  Create a Django app that takes an MSISDN (Mobile Station International Subscriber Directory Number) as an input and returns information such as:
- MNO (Mobile Network Operator) identifier
- country dialling code, subscriber number and
- country identifier (ISO 3166-1-alpha-2)


## Project requirements
Running this project locally requires installation of Docker Desktop. Since development is all done through Docker, there are no other local installations needed.

I personally used a version of Docker suitable for Ubutu WSL, but the OS should not matter. Versions I installed were:
- Docker v24.0.6
- Docker-compose v2.20.2

## Getting started with local development
Run ```docker build .``` to build the docker image.

Run ```docker-compose build``` to run the above command, but use the docker-compose.yml file.

## Linting Locally

Flake8 is used for linting the code in this project. To run, from the main project directory run:
```
docker-compose run --rm app sh -c "flake8"
```

## Testing Locally
Run:
```
docker-compose run --rm app sh -c "python manage.py test"
```

## Run Project with Docker Compose

After building the docker image, run: ```docker-compose up```
Then go to [http://localhost:8000](http://localhost:8000) to see the app in development.

Go to test admin functionality go to: [http://localhost:8000/admin](http://localhost:8000/admin)
Create a superuser in the terminal by entering ```docker-compose run --rm app sh -c "python manage.py createsuperuser```
Then login to the admin page using the admin credentials you provided.

## Documentation Page
Swagger is used in this project to generate a documentation page for the API. This can be accessed at [http://localhost:8000/api/docs](http://localhost:8000/api/docs).


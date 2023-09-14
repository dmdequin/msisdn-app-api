# msisdn-app-api
MSISDN App API

## Getting started
Run ```docker build .``` to build the docker image.

Run ```docker-compose build``` to run the above command, but use the docker-compose.yml file.

## Linting Locally

Flake8 was used for linting the code in this project. To run, from the main project directory enter:
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
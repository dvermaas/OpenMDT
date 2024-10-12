# DjangoPolls

DjangoPolls is a Django web-application that simulates a mobile data terminal (MDT) for law-enforcement. 
It's main purpose is exploring and learning more about Django. Currently the application uses a s3 bucket, Postgres
database, and a full CI/CD pipeline for containerised deployments using Docker.

# Run the server

To run the application either:

- create a .env file in the root
- run `python manage.py migrate`
- run `python manage.py runserver`

Or:
- install docker
- run 'docker compose up --build'
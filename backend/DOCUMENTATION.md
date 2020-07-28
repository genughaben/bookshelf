# Bookshelf API Backend

## Intro

This projects provides a API to view lists or individual books, search books, create, delete and update books entries saved in a Flask-SQLAlchemy managed database.
Here, we use a PostgreSQL-Database underneath.

## Getting Started

### Prerequisits:

* Python3
* PostgreSQL (locally or docker) exposed at 5432 

### Setup

```shell script
> python3 -m venv venv
> sourve venv/bin/activate
> pip install -r requirements
```

Now, you are good to go and continue as you would any time you start the app.

### Start

#### 1 Check if PostgreSQL is running

Check if PostgreSQL is ready, if installed locally

```shell script
> systemctl status postgresql
```

Check if PostgreSQL is ready, if running in docker:

```shell script
> docker ps
```

#### 2 Start your App

```shell script
> export FLASK_APP=flaskr
> export FLASK_ENV=development
> flask run
 
```

### Base URL

To access the running APP locally, you will find it at: localhost:5000

### API Keys /Authentication (if applicable)

No API Keys or Authentication required, for now. But you could easily add it using e.g. Flask-BasicAuth if you like.

### Errors



Response codes
Messages
Error types
Resource endpoint library
Organized by resource
Include each endpoint
Sample request
Arguments including data types
Response object including status codes and data types

Contribute


Project Title

Description of project and motivation
Screenshots (if applicable), with captions
Code Style if you are following particular style guides
Getting Started

Prerequisites & Installation, including code samples for how to download all pre-requisites
Local Development, including how to set up the local development environment and run the project locally
Tests and how to run them
API Reference. If the API documentation is not very long, it can be included in the README

Deployment (if applicable)

Authors

Acknowledgements

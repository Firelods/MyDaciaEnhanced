# Backend API Documentation

## Architecture
The back-end is a REST API built with Python and Flask. It handles data processing, server-side logic, and interactions with the vehicle's systems.

### Endpoints
All endpoints are visible [here](Endpoints.md)


### Files {collapsible="true"}
#### Account.py
This file contains the logic for creating and managing user accounts.

#### Vehicle.py
This file contains the logic for interacting with the vehicle's systems.

#### Routes.py
This file contains the logic for handling HTTP requests.

#### Middleware.py
This file contains the logic for handling HTTP requests before they are passed to the routes.

#### Database.py
This file contains the logic for interacting with the database.

#### Scheduler.py
This file contains the logic for scheduling tasks with BackgroundScheduler.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installing
- Docker Compose: `docker compose up -d` (the `-d` flag is optional and runs the application in detached mode)

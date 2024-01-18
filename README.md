# MyDaciaEnhanced

## Introduction
*MyDaciaEnhanced* is a project aimed at enhancing the user experience for Dacia vehicle owners. This repository includes both the front-end and back-end components necessary to deliver a comprehensive solution.

The original application is available on the [Dacia website](https://www.dacia.fr/decouvrez-mydacia.html) 

## Benefits
The main benefits of this project are:
- **Charge Schedule**: The user can schedule the charging of the vehicle's battery, which is useful for taking advantage of off-peak electricity rates.
- **A/C Schedule**: The user can schedule the activation of the vehicle's air conditioning system, which is useful for cooling the vehicle before a trip.

MyDacia only allows users to charge their vehicle's battery or activate the air conditioning system immediately. This project allows users to schedule these actions for a later time.



### Front-End
The front-end is developed using Angular and provides a user-friendly interface for interacting with the vehicle's features.

### Back-End
The back-end, built with Python, handles data processing, server-side logic, and interactions with the vehicle's systems.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them:
- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)
- [Angular CLI](https://cli.angular.io/)

### Installing
A step by step series of examples that tell you how to get a development environment running:

1. Clone the repo: `git clone https://github.com/Firelods/MyDaciaEnhanced.git`
2. Navigate to the project directory: `cd MyDaciaEnhanced`
3. Install dependencies:
   - Front-end: `cd front && npm install`
   - Back-end: `docker compose pull`

### Running

#### Front-End
1. Navigate to the front-end directory: `cd front`
2. Run the application: `ng serve`
3. Navigate to `http://localhost:4200/`

#### Back-End
1. Navigate to the back-end directory: `cd api`
2. Run the application: `docker compose up -d` (the `-d` flag is optional and runs the application in detached mode)
3. Send requests to `http://localhost:5000/`


## Built With
- [Angular](https://angular.io/) - Front-end framework
- [Python](https://www.python.org/) - Back-end language
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Back-end framework
- [Docker](https://www.docker.com/) - Containerization
- [Docker Compose](https://docs.docker.com/compose/) - Container orchestration

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [HACF](https://github.com/hacf-fr/renault-api) for providing the API used to interact with the vehicle's systems

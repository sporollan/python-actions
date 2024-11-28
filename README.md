## Python Project with Docker and CI/CD

Minimal Python application that runs its tests in a Dockerized environment.
Makes use of Github Actions workflow to automate testing on every push.

### Overview
The project consists of three Python modules and their
corresponding unit tests.
The tests can be executed locally, inside a container,
or automatically via GitHub Actions.

### Running with Docker
1. Build the image:
    ` docker build -t python-actions-run-tests . `
2. Run tests inside container:
    ` docker run --rm python-actions-run-tests `
    
Or alternatively, execute run_tests.sh

### Workflow
As triggered on every push
1. Build Docker Image
2. Run unit tests in the container
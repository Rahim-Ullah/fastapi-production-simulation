# FastAPI Production Simulation

A small, practical FastAPI project created to explore what it feels like to take an API from a local development environment and run it in production.

The application is intentionally simple: it exposes a friendly `/home` endpoint that confirms the service is up and responding. The main goal is not complexity, but learning the essential path from writing an API to deploying it and testing it on a real hosting platform.

## Live Demo

The deployed application is available here:

**[Open the live FastAPI app](https://fastapi-production-simulation.onrender.com/home)**

When the service is running correctly, the `/home` endpoint returns:

```json
{
  "Welcome :": "To testing in production tutorial!"
}
```

## What This Project Demonstrates

- Creating a minimal API with **FastAPI**
- Defining a simple HTTP `GET` route
- Running the application with **Uvicorn**
- Preparing Python dependencies for deployment
- Deploying a FastAPI service to **Render**
- Verifying that an API works outside the local development environment

## Tech Stack

- **Python**
- **FastAPI** — the web framework used to build the API
- **Uvicorn** — the ASGI server used to run the application
- **Render** — the production hosting platform

## Project Structure

```text
.
├── main.py
├── requirements.txt
├── example.env
└── README.md
```

### `main.py`

Contains the FastAPI application and the `/home` route.

### `requirements.txt`

Lists the Python packages required to install and run the project.

### `example.env`

Acts as a reference for environment variables that may be needed as the project grows. It does not contain real secrets.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rahim-Ullah/fastapi-production-simulation.git
cd fastapi-production-simulation
```

### 2. Create and activate a virtual environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the development server

```bash
uvicorn main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000/home
- Interactive Swagger documentation: http://127.0.0.1:8000/docs

## API Endpoint

### `GET /home`

Returns a simple welcome message to confirm that the application is available.

## Why This Repository Exists

Production deployment can feel intimidating when you are only familiar with running code on your own computer. This project keeps the application deliberately small so the deployment process is easier to understand: build a route, install the dependencies, start the server, deploy it, and test the live result.

It is a useful starting point for experimenting with production concepts before adding larger features such as databases, authentication, background tasks, structured logging, monitoring, or automated deployment workflows.

## Future Improvements

Some natural next steps for this project include:

- Add health-check and version endpoints
- Introduce request and response models with Pydantic
- Add automated tests with `pytest`
- Add structured logging and error handling
- Connect the API to a database
- Add a CI/CD workflow with GitHub Actions

## License

No license has been specified yet.

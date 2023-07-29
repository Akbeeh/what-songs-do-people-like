# What songs do people like ?
Here's my first big personal project to develop my skills and become a good Data Engineer.

## Overview
The goal of the project is to create a web application that allows users to search for songs, view their ratings on Spotify and Apple Music, and analyze the number of listens per country/region. Users will have their own accounts where they can like or dislike songs.

## Steps followed to create the project

1. Poetry project for the backend
```bash
# `poetry init --no-interaction` to initialize a pre-existing project
poetry new backend --name="app"
cd backend
poetry add fastapi sqlalchemy psycopg2-binary uvicorn pydantic requests spotipy python-dotenv
# `poetry shell` to access the environment in the terminal
```

2. Backend files
```bash
mkdir dags sql
touch dags/spotify_dag.py dags/__init__.py
touch sql/create_tables.sql
cd app
mkdir credentials database routers
touch main.py dependencies.py
touch credentials/auth.py credentials/credentials.json
touch database/database.py database/models.py database/repositories.py database/schemas.py
touch routers/songs.py routers/users.py routers/__init__.py
```

- `backend/app/main.py`: Write the FastAPI application code.
- `backend/app/dependencies.py`: Define the API dependencies.
- `backend/app/credentials/auth.py`: Generate, retrieve and save credentials to access the Spotify API.
- `backend/app/database/database.py`: Define all functions related to the connection and manipulation of the database.
- `backend/app/database/models.py`: Define the SQLAlchemy models of the tables for the database.
- `backend/app/database/repositories.py`: Implement the data access layer.
- `backend/app/database/schemas.py`: Define the SQLAlchemy schemas for the database.
- `backend/app/routers/songs.py`: Define the API routes for songs.
- `backend/app/routers/users.py`: Define the API routes for users.

3. Vite project for the frontend
```bash
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install -S react react-dom react-router-dom leaflet react-leaflet primereact primeflex primeicons @mui/material @mui/icons-material @emotion/react @emotion/styled
```

4. Set up the PostgreSQL database
```bash
# sudo service postgresql status
sudo service postgresql restart
sudo su - postgres
psql
CREATE DATABASE wsdpldb;
CREATE USER wsdpl WITH PASSWORD 'wsdplPW';
GRANT ALL PRIVILEGES ON DATABASE wsdpldb TO wsdpl;
# TRUNCATE TABLE "table_name;" to reset the table
# ALTER TABLE "table_name" ADD COLUMN "column_name" VARCHAR NOT NULL; to add info

# "\c wsdpldb" to connect to the database
# "\l" to check databases
# "\q" to quit
# "exit" to quit

# from postgres you can generate a PostgreSQL database dump file that needs to be moved in "sql" folder
pg_dump -d wsdpldb -s -f create_tables_wsdpl.sql
```

5. Set up Airflow
```bash
# At the project root
# Everytime for a new terminal, must execute the line below to put correctly the AIRFLOW_HOME
export AIRFLOW_HOME=$(pwd)/airflow
airflow db init
# And here replace the generated airflow.cfg by the personal one
cp -f backend/airflow.cfg airflow/
airflow users create \
    --username admin \
    --firstname William \
    --lastname M \
    --role Admin \
    --email Akbeeeh@gmail.com \
    --password admin
airflow webserver -p 8080
airflow scheduler
```

6. Run the backend and frontend (without Docker)
```bash
# In the backend
poetry run uvicorn app.main:app --reload

# In the frontend
npm run dev
```

7. Docker
There are three different Dockerfile for the `backend`, `frontend` and `Airflow`.
At the `root` project directory, we can find a `docker-compose.yml` that is searched and executed when the following command is run:
```bash
# At the root
docker compose up
```

Notices:
- As I'm using `python:3.10-slim`, it is necessary to give credentials (connect with a Docker account) to be able to pull the Python right version.
- If there's a problem with credentials, beforehand do 
```bash
docker pull python:3.10-slim
docker pull node:20.2.0-slim
docker pull postgres:14.8-alpine
```

## Issues I encountered (by the way mostly or totally with Docker)
- Airflow (with Docker): I couldn't figure out how to link correctly the Airflow server with FastAPI using custom Python packages, as it use handmade functions to reload the Spotify API token (in order to be able to do requests... + expires every hour)
- Vite project (with Docker): I guess it's better to put directly http://localhost:8080/ in .tsx files (e.g. `frontend/src/pages/TopSongs.tsx`) that communicate with the backend, instead of using a proxy (by adding it in the `frontend/vite.config.ts`)
- PostgreSQL (with Docker): in the `DATABASE_URL` parameter, the network location configured must be carefully examinated. Indeed, when the app runs locally it's **localhost**, but with Docker, the network location should be taken from the PostgreSQL's location and informed to the backend (and therefore it's not **localhost** but the name of the service, here **postgres**)
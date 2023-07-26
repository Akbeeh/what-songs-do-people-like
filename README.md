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
poetry add fastapi sqlalchemy psycopg2-binary uvicorn pydantic requests spotipy
# `poetry shell` to access the environment in the terminal
```

2. Backend files
```bash
mkdir database routers
cd app
touch main.py dependencies.py models.py repositories.py
cd ..
touch routers/routes.py routers/users.py
touch database/create_tables.sql
```

- `backend/app/main.py`: Write the FastAPI application code.
- `backend/app/dependencies.py`: Define the API dependencies.
- `backend/app/models.py`: Define the SQLAlchemy models for the database.
- `backend/app/schemas.py`: Define the SQLAlchemy schemas for the database.
- `backend/app/repositories.py`: Implement the data access layer.
- `backend/app/routers/songs.py`: Define the API routes for songs.
- `backend/app/routers/users.py`: Define the API routes for users.

3. Vite project for the frontend
```bash
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install -S react-router-dom primereact primeflex primeicons @mui/material @emotion/react @emotion/styled react-simple-maps
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
```

5. Set up Airflow
```bash
# In the backend
# In fact, the ariflow.cfg must be placed in the $AIRFLOW_HOME folder (generally ~/airflow)
airflow db init
airflow users create \
    --username admin \
    --firstname William \
    --lastname M \
    --role Admin \
    --email Akbeeeh@gmail.com
airflow webserver
airflow scheduler
```

6. Run the backend and frontend
```bash
# In the backend
uvicorn app.main:app --reload

# In the frontend
npm run dev
```

7. Docker

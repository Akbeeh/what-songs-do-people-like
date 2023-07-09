# What songs do people like ?

Here's my first big personal project to develop my skills and become a good Data Engineer.

## Overview

The goal of the project is to create a web application that allows users to search for songs, view their ratings on Spotify and Apple Music, and analyze the number of listens per country/region. Users will have their own accounts where they can like or dislike songs.

## Steps followed to create the project

1. Poetry project for the backend
```bash
# `poetry init --no-interaction` for initialising a pre-existing project
poetry new backend --name="app"
cd backend
poetry add fastapi sqlalchemy psycopg2-binary uvicorn
```

2. Backend files
```bash
mkdir database
cd app
touch main.py models.py repositories.py routes.py
cd ..
touch database/create_tables.sql
```

- `backend/app/main.py`: Write the FastAPI application code.
- `backend/app/models.py`: Define the SQLAlchemy models for the database.
- `backend/app/repositories.py`: Implement the data access layer.
- `backend/app/routes.py`: Define the API routes.

3. Vite project for the frontend
```bash
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
```

4. Set up the PostgreSQL database
```bash
# sudo service postgresql status
sudo service postgresql restart
sudo su - postgres
psql
# "\q" to quit
# "exit" to quit
```

5. Run the backend and frontend
```bash
# In the backend
uvicorn app.main:app --reload

# In the frontend
npm run dev
```

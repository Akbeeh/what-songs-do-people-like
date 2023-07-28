# Python version
FROM python:3.10-slim

# Configure Poetry
ENV POETRY_VERSION=1.5.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install Poetry separated from the system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Set the working directory in the container
WORKDIR /backend

# Copy the backend source code into the container 
# (including the pyproject.toml and poetry.lock files)
COPY . .

# Replace the database_url in the .env file
ARG DATABASE_URL="postgresql://wsdpl:wsdplPW@postgres:5432/wsdpldb"
RUN sed -i "s|^DATABASE_URL=.*|DATABASE_URL=$DATABASE_URL|" .env

# Install project dependencies
RUN poetry install --no-dev --no-root

# Expose the port on which the backend app is running
EXPOSE 8000

# Command to run the backend application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

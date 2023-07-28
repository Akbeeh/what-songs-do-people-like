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
WORKDIR /

# Copy the backend source code into the container 
# (including the pyproject.toml and poetry.lock files)
COPY backend/ /backend/
COPY backend/pyproject.toml backend/poetry.lock /

# Install project dependencies
RUN poetry install --no-dev --no-root

# Set the AIRFLOW_HOME environment variable to specify the Airflow configuration directory
ENV AIRFLOW_HOME=/airflow

# Set the AIRFLOW__CORE__SQL_ALCHEMY_CONN environment variable to specify where the Airflow should be connected with
# ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql://wsdpl:wsdplPW@postgres:5432/wsdpldb

# Initialize the Airflow database
RUN poetry run airflow db init

# Copy your custom airflow.cfg to the container
COPY backend/airflow.cfg ${AIRFLOW_HOME}/

# Set a build argument for the admin password (you can change 'admin' to your desired password)
ARG ADMIN_PASSWORD=admin

# Create an admin user
# RUN poetry run airflow users create \
#     --username admin \
#     --firstname William \
#     --lastname M \
#     --role Admin \
#     --email Akbeeeh@gmail.com \
#     --password $ADMIN_PASSWORD

# Expose the port your Airflow web server is running on (default is 8080)
EXPOSE 8080

# Start the web server and scheduler
CMD ["sh", "-c", "poetry run airflow webserver --port 8080 & poetry run airflow scheduler & wait"]
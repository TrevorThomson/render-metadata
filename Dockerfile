
## python 3.12+ removes support for asyncore which is used by cassandra
## as of this writing, apk installing libev for events in python 3.12 doesn't seem
## to work -- cassandra-driver still complains that it can't find libev
FROM python:3.11-alpine AS production

ARG APPNAME
ARG CASSANDRA_ADDRS

EXPOSE 80

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements before installing app since requirements are less likely to change
COPY $APPNAME/requirements.txt app_requirements.txt
COPY database/requirements.txt db_requirements.txt
RUN python -m pip install -r ./app_requirements.txt -r ./db_requirements.txt

WORKDIR /app
COPY $APPNAME /app/$APPNAME
COPY database /app/database

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# expose APPNAME env. var. for CMD
ENV APPNAME=$APPNAME
ENV CASSANDRA_ADDRS=$CASSANDRA_ADDRS

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD gunicorn --bind 0.0.0.0:80 "$APPNAME:create_service($CASSANDRA_ADDRS)"

FROM production AS testing

COPY tests /app/tests

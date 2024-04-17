
## python 3.12+ removes support for asyncore which is used by cassandra
## as of this writing, apk installing libev for events in python 3.12 doesn't seem
## to work -- cassandra-driver still complains that it can't find libev
FROM python:3.11-alpine

ARG APPNAME

EXPOSE 80

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements before installing app since requirements are less likely to change
COPY $APPNAME/requirements.txt .
RUN python -m pip install -r ./requirements.txt

WORKDIR /app
COPY $APPNAME /app/$APPNAME

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# expose APPNAME env. var. for CMD
ENV APPNAME=$APPNAME

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD gunicorn --bind 0.0.0.0:80 "$APPNAME:create_service()"

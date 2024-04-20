
Python unittest module
======================

Running locally
---------------
To run the api tests locally, a local cassandra ports must be exposed in the local host.
With docker:
- See: https://hub.docker.com/_/cassandra
- docker run --detach --name cassandra-1 -p 7000:7000 -p 9042:9042 cassandra:4.1

With docker-compose.yml:
- docker compose build
- docker compose up
- curl -X POST -H "Content-Type: application/json" -d '{"name": "myshot", "showname": "myshow", "startframe": 101, "endframe": 110}' http://localhost:8080/shot


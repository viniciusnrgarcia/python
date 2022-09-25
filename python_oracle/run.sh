#!/bin/bash
docker run -d --env-file ora_db_env.dat -p 1521:1521 --name oracle-std --shm-size="8g" container-registry.oracle.com/database/standard:latest

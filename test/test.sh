#!/bin/bash
docker-compose --env-file test/env.docker -f docker-compose.yml -f test/docker-compose.yml up --build -V --exit-code-from pdsconfig-test

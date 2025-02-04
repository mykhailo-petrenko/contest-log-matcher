#!/usr/bin/env bash

VERSION=$(head -n 1 version.txt)

docker image push ur3amp/contest-log-matcher:latest
docker image push ur3amp/contest-log-matcher:"${VERSION}"

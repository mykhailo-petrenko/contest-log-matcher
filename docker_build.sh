#!/usr/bin/env bash

VERSION=$(head -n 1 version.txt)

docker buildx build --platform=linux/amd64 \
  -t ur3amp/contest-log-matcher:latest \
  -t ur3amp/contest-log-matcher:"${VERSION}" .

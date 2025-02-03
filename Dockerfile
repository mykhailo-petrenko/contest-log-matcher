FROM python:3.11.10-alpine3.20 AS build
LABEL authors="mykhailo@petrenko.nl"

WORKDIR /opt/contest-log-matcher
COPY requirements.txt ./

RUN apk add libxml2-dev libxslt-dev

RUN pip install -r requirements.txt


FROM build

COPY . .

ENTRYPOINT ["/opt/contest-log-matcher/entrypoint.sh"]

FROM python:3.11.10-alpine3.20 AS build
LABEL authors="mykhailo@petrenko.nl"

WORKDIR /opt/contest-log-matcher
COPY requirements.txt ./

RUN pip install -r requirements.txt


FROM build

COPY api ./api
COPY cabrillo ./cabrillo
COPY storage ./storage
COPY utils ./utils
COPY entrypoint.sh ./

ENTRYPOINT ["/opt/contest-log-matcher/entrypoint.sh"]
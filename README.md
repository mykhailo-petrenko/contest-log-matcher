# Log Matcher 
This is a REST service for a contest log scoring (without cross-checking yet).

[https://contest-log-matcher.petrenko.nl/](https://contest-log-matcher.petrenko.nl/)

## Environment
Install venv
```shell
python -m venv venv
```

Activate venv
```shell
source venv/bin/activate
pip install -r requirements.txt
```

## Endpoints

### `/log/validate`
Just validate cab log

### `/log/stats`
Validate log and calculate scores

## @TODO:
### v1.x
- [x] Validation method. Takes text as an input and return OK and serialized log in case of success or Error with a basic error description.
- [x] Setup REST server. Use FastAPI, Uvicorn.
- [x] Expose validation method via REST api.
- [x] Design contest log submission and contest evaluation API
- [x] LOG: Submit log to check results

### v2.x
- [ ] Admin endpoint: Contest create, list, get, archive
- [ ] Choose DB: sqlite?

## Build docker
```shell
docker buildx build --platform=linux/amd64 \
  -t ur3amp/contest-log-matcher:latest \
  -t ur3amp/contest-log-matcher:1.2.2 .
```


```shell
docker image push ur3amp/contest-log-matcher:latest
docker image push ur3amp/contest-log-matcher:1.2.2
```

## Run in docker

```shell
docker run --rm -p "8080:8080" ur3amp/contest-log-matcher:latest 
```

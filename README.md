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
- [ ] Contest config in YARN format
- [ ] Flexible rules configuration. Composite rules to 
- [ ] Admin endpoint: Contest create, list, get, archive
- [ ] Choose DB: sqlite?

### v3.x
- [ ] Visual editor for contest rules

## Build docker

Increment (check) the `version.txt` before build.

```shell
source docker_build.sh
```

```shell
source docker_push.sh
```

## Run in docker

```shell
docker run --rm -p "8080:8080" ur3amp/contest-log-matcher:latest 
```

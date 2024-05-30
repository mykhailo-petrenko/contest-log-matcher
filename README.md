# Log Matcher

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

## @TODO:
 - Validation method. Takes text as an input and return OK and serialized log in case of success or Error with a basic error description.
 - Setup REST server. Use FastAPI, Uvicorn.
 - Expose validation method via REST api.
 - Design contest log submission and contest evaluation API
    - Contest: create?, list, get
    - LOG: Submit log to active contest, check results
    - Statistic: Active contest, Archive ?
    - Evaluator (Admin API)
 - Choose DB 
 - ...

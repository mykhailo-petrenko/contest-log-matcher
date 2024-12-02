from fastapi import FastAPI, Body

from api import log

app = FastAPI()
# app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(log.router)

@app.get("/")
async def index():
    return {"message": "Hello World"}
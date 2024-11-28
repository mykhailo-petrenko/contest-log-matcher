import uvicorn
from fastapi import FastAPI

app = FastAPI()


# noinspection PyPackageRequirements
@app.get("/")
async def index():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8073, reload=True)

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from api import log
from api.version import version

app = FastAPI(
    title="Contest Log Mather",
    version=version(),
    description="Validate and evaluate cab logs",
    # dependencies=[Depends(get_query_token)]
)

app.include_router(log.router)


@app.get("/")
async def index():
    return RedirectResponse("/docs")

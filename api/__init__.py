from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse, RedirectResponse

from api import log

app = FastAPI()
# app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(log.router)

def generate_openapi_schema():
    """
    Generate the OpenAPI schema for the FastAPI application.
    """
    return get_openapi(
        title="Contest Log Mather",
        version="1.2.1",
        description="Validate and evaluate cab logs",
        routes=app.routes,
    )

@app.get("/openapi.json")
def get_openapi_endpoint():
    """
    Retrieve the generated OpenAPI schema.
    """
    return JSONResponse(content=generate_openapi_schema())

@app.get("/")
async def index():
    return RedirectResponse("/docs")

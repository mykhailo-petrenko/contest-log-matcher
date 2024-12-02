from fastapi import APIRouter, Body

from api.contest.rules import Rules
from api.contest.scoring import Scoring
from cabrillo.cabrillo.errors import InvalidLogException, InvalidQSOException
from cabrillo.cabrillo.parser import parse_log_text
from storage import get_contest_rules_config

router = APIRouter(
    prefix="/log",
    tags=["log"],
    dependencies=[], #Depends(get_token_header)
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def log_default():
    return {"message": "I'm log endpoint"}


@router.post("/validate")
async def log_evaluate(body: str = Body(media_type='text/plain')):
    try:
        log = parse_log_text(body, ignore_unknown_key=True, check_categories=False)
    except InvalidLogException as error:
        return {
            "status": "error",
            "errorType": "InvalidLogException",
            "message": str(error)
        }
    except InvalidQSOException as error:
        return {
            "status": "error",
            "errorType": "InvalidQSOException",
            "message": str(error)
        }
    except Exception as error:
        return {
            "status": "error",
            "errorType": "general",
            "message": str(error)
        }

    return {
        "status": "ok",
        "log": log,
    }

@router.post("/stats")
async def log_stats(body: str = Body(media_type='text/plain')):
    try:
        log = parse_log_text(body, ignore_unknown_key=True, check_categories=False)
    except InvalidLogException as error:
        return {
            "status": "error",
            "errorType": "InvalidLogException",
            "message": str(error)
        }
    except InvalidQSOException as error:
        return {
            "status": "error",
            "errorType": "InvalidQSOException",
            "message": str(error)
        }
    except Exception as error:
        return {
            "status": "error",
            "errorType": "general",
            "message": str(error)
        }

    rules_config = get_contest_rules_config()
    rules = Rules(rules_config)
    scoring = Scoring(rules)

    results = scoring.stats(log)

    return {
        "status": "ok",
        "results": results,
        "log": log,
    }
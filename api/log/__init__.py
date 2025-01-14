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
    """
    Validate log and turns

    ```
        {
            "status": "ok",
            "log": dict() // parsed log in json format
        } in case of success
    ```
    or
    ```
        {"status": "error", "errorType": str, "message": str,}
    ```
    """
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


@router.post("/stats/{contest_id}")
async def log_stats(contest_id: str, body: str = Body(media_type='text/plain')):
    """
    Evaluate and validate contest log.
    Returns json response.


    ```
    {
        "status": "ok" | "error",
        "message": string, // in case of error
        "results": {
            "score": int, // evaluated score points
            "total": int, // total qso count
            "band80m": int, // total qso per 80m band count
            "band40m": int, // total qso per 40m band count
            "band20m": int, // total qso per 20m band count
        },
        "log": dict() // parsed log in json format
    }
    ```
    """

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

    rules_config = get_contest_rules_config(contest_id)

    if not rules_config:
        return {
            "status": "error",
            "errorType": "InvalidContestId",
            "message": "Please provide valid contest id"
        }

    rules = Rules(rules_config)
    scoring = Scoring(rules)

    results = scoring.stats(log)

    return {
        "status": "ok",
        "results": results,
        "log": log,
    }

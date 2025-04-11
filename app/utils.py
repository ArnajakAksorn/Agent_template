# app/utils.py
from typing import Any, Dict
from fastapi import Request, HTTPException

def per_request_config_modifier(
    config: Dict[str, Any], request: Request
) -> Dict[str, Any]:
    config = config.copy()
    configurable = config.get("configurable", {})

    user_id = request.cookies.get("user_id", None)
    if user_id is None:
        raise HTTPException(
            status_code=400,
            detail="No user id found. Please set a cookie named 'user_id'.",
        )
    configurable["user_id"] = user_id
    config["configurable"] = configurable
    return config

# app/api.py
from fastapi import FastAPI
from langserve import add_routes

from core.agent_call import pirate_chain_with_history
from app.utils import per_request_config_modifier  # rename better

def setup_routes(app: FastAPI):
    add_routes(
        app,
        pirate_chain_with_history,
        per_req_config_modifier=per_request_config_modifier,
        disabled_endpoints=["playground", "batch"],
    )

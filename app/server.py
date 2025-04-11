# app/server.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import setup_routes
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Genie Server",
    version="0.1",
    description="Internal GPT",
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

setup_routes(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
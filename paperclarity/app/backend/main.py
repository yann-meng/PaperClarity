from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from paperclarity.app.backend.api.routes import router

app = FastAPI(title="PaperClarity API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

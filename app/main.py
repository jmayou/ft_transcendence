from fastapi import FastAPI

from .offline import router as offline_router
from .online import router as online_router


app = FastAPI()
app.include_router(offline_router)
app.include_router(online_router)

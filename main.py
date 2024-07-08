from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from endpoints import views_router
from config import MEDIA_DIR


app = FastAPI(title="YouTube downloader")


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/app")


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.mount("/media", StaticFiles(directory=MEDIA_DIR))

app.include_router(views_router)

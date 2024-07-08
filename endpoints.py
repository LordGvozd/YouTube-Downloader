from typing import Annotated

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from fastui import FastUI, AnyComponent, prebuilt_html
from fastui.forms import fastui_form
from fastui.events import GoToEvent
from fastui import components as c
from starlette.responses import FileResponse

from youtube.youtube_downloader import download_video, download_audio

from schemas import DownloadRequest, DownloadType

views_router = APIRouter(prefix="", tags=["Views"])


@views_router.post("/download/")
async def download(form: Annotated[DownloadRequest, fastui_form(DownloadRequest)]) -> list[AnyComponent]:
    file="/app"
    if form.download_type == DownloadType.video:
        file = download_video(form.link)
    elif form.download_type == DownloadType.audio:
        file = download_audio(form.link)
    return [c.FireEvent(event=GoToEvent(url=file, target='_blank'))]


@views_router.get("/api/app/", response_model=FastUI, response_model_exclude_none=True)
async def index() -> list[AnyComponent]:
    return [
        c.Page(components=[
            c.Div(class_name="d-flex justify-content-center",
                  components=[
                      c.Div(class_name="d-flex w-75 h100 p-5 justify-content-start flex-column mx-10",
                            components=[
                                c.Heading(text="YouTube downloader", level=1, class_name="text-center"),
                                c.ModelForm(
                                    class_name="mt-5",
                                    model=DownloadRequest,
                                    submit_url="/download/"
                                )
                            ])
                  ])
        ]),
    ]


@views_router.get("/app/{path:path}")
async def html_page() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="YouTube downloader"))

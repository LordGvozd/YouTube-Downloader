from enum import Enum

from pydantic import BaseModel


class DownloadType(Enum):
    video = "video"
    audio = "audio"


class DownloadRequest(BaseModel):
    link: str
    download_type: DownloadType

class Link(BaseModel):
    link: str

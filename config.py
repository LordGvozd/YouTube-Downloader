from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).parent.resolve()

MEDIA_DIR = ROOT_DIR / "media"

VIDEO_DIR = ROOT_DIR / "media" / "video"
AUDIO_DIR = ROOT_DIR / "media" / "audio"

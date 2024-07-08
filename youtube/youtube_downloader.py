from os import PathLike

from pytube import YouTube

from config import VIDEO_DIR, AUDIO_DIR


def download_video(youtube_video_link: str) -> str:
    youtube = YouTube(youtube_video_link)

    video = youtube.streams.get_highest_resolution()
    video_output_path: PathLike[str] = VIDEO_DIR / video.default_filename

    video.download(filename=str(video_output_path))

    return str("/media/video/" + video.default_filename)


def download_audio(youtube_video_link: str) -> str:
    youtube = YouTube(youtube_video_link)

    audio = youtube.streams.get_audio_only()

    audio_output_path: PathLike[str] = AUDIO_DIR / audio.default_filename.replace("mp4", "mp3")

    audio.download(filename=str(audio_output_path))

    return str("/media/audio/" + audio.default_filename.replace("mp4", "mp3"))




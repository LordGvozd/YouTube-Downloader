FROM python:3.11-buster

ENV PYTHONUNBUFFERED=1


WORKDIR /app

RUN apt-get update && apt install python3-dev -y


RUN pip install --upgrade pip
RUN python -m venv .venv
RUN ["/bin/bash", "-c", "source .venv/bin/activate"]
RUN pip install poetry
ADD pyproject.toml .
RUN poetry install --no-root --no-interaction --no-ansi
RUN python3 -m pip install --upgrade pytube
EXPOSE 8000


COPY . .

RUN mv ./cipher.py ./.venv/lib/python3.11/site-packages/pytube/cipher.py




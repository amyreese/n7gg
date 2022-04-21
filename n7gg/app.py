# Copyright 2022 John Reese
# Licensed under the MIT license

from typing import Optional

from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, redirect, text

DEFAULT_KEY = "home"
MESSAGES = {
    "index.php": "Nice try",
    "index.html": "Simple",
}
URLS = {
    "home": "jreese.sh",
    "thx": "thx.omnilib.dev",
}

for key in URLS:
    if not URLS[key].startswith("https://"):
        URLS[key] = "https://" + URLS[key]


def response(key: Optional[str] = None) -> HTTPResponse:
    key = key or DEFAULT_KEY

    if key in URLS:
        return redirect(URLS[key])

    if key in MESSAGES:
        return text(MESSAGES[key])

    return text("four oh four", status=404)


app = Sanic("n7gg")


@app.get("/")
async def nothing(request: Request) -> HTTPResponse:
    return response()


@app.get("/<key:path>")
async def main_handler(request: Request, key: str) -> HTTPResponse:
    return response(key)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4242, workers=1)

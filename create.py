# create.py

import os


import json
from pathlib import Path


import openai


PROMPT = "A car on a car"

DATA_DIR = Path.cwd() / "responses"

DATA_DIR.mkdir(exist_ok=True)


# openai.api_key = "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"

# My API Key
openai.api_key = "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"


response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)




file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)

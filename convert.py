import json
from base64 import b64decode
from pathlib import Path
import os
import glob


def get_json_file_name():
    directory = os.getcwd() + "\\responses"
    full_path_file = glob.glob(directory + "/*")[0]
    name = os.path.basename(full_path_file)

    return name


json_file_name = get_json_file_name()

DATA_DIR = Path.cwd() / "responses"
JSON_FILE = DATA_DIR / json_file_name
IMAGE_DIR = Path.cwd() / "images"






IMAGE_DIR.mkdir(parents=True, exist_ok=True)


with open(JSON_FILE, mode="r", encoding="utf-8") as file:
    response = json.load(file)


for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)

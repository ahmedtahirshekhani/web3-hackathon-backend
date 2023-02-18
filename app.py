import re
from datetime import datetime

from flask import Flask, request
import os
import glob
import matplotlib.pyplot as plt
import openai

from flask import send_file


app = Flask(__name__)


# openai.api_key = "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"

# PROMPT = "A car on a plane"

# DATA_DIR = Path.cwd() / "responses"

# DATA_DIR.mkdir(exist_ok=True)


# response = openai.Image.create(
#     prompt=PROMPT,
#     n=1,
#     size="256x256",
#     response_format="b64_json",
# )


# file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

# with open(file_name, mode="w", encoding="utf-8") as file:
#     json.dump(response, file)


@app.route("/", methods=["GET"])
def home():

    return "Ok", 200


@app.route("/api/ai", methods=["GET"])
def get_image():
    param = request.args.get("prompt")
    print(param)
    directory = os.getcwd() + "\\images"

    full_path_file = glob.glob(directory + "/*")[0]

    return send_file(full_path_file, mimetype='image/png')


# @app.route("/hello/<name>")
# def hello_there(name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     # print(name)

#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return content

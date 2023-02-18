import re
from datetime import datetime

from flask import Flask
import os
import glob
import matplotlib.pyplot as plt


from flask import send_file

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():

    return "Ok", 200


@app.route("/api/ai", methods=["GET"])
def get_image():

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

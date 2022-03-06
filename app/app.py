from flask import Flask, request, abort, redirect
import os
import re
import time
import json
import random

import illumi
import anicat
import space
import status
from content_type import *

app = Flask(__name__)

app.register_blueprint(illumi.blueprint)
app.register_blueprint(anicat.blueprint)
app.register_blueprint(space.blueprint)
app.register_blueprint(status.blueprint)

@app.route("/")
def index():
    with open("index.html", "r") as f:
        with open("musiclist.json", "r") as l:
            json_data = l.read()
            json_data = re.sub(r"/\*[\w ]*\*/", "", json_data) #清除注释
            lis = json.loads(json_data)
            url = random.choice(lis)
        html = f.read()
        html = html.replace("{music_url}", url)
        return html

@app.route("/<file>")
def file(file):
    if os.path.isfile(file) == False:
        abort(404)
    if file == "index.html":
        return redirect("/")
    with open(file, "rb") as f:
        return f.read(), 200, {"Content-Type": content_type(file)}

@app.route("/resource/<file>")
def resource(file):
    if os.path.isfile(f"resource/{file}") == False:
        abort(404)
    with open(f"resource/{file}", "rb") as f:
        if request.args.get("type") == "download":
            return f.read(), 200, {"Content-Type": "application/octet-stream"}
        return f.read(), 200, {"Content-Type": content_type(file)}

@app.route("/image/<file>")
def image(file):
    if os.path.isfile(f"image/{file}") == False:
        abort(404)
    with open(f"image/{file}", "rb") as f:
        return f.read(), 200, {"Content-Type": content_type(file)}

@app.route("/post", methods = ["POST"])
def get_post():
    if request.form.get("method") == "storage":
        with open(request.form.get("file"), "a+") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
            f.write(request.form.get("data") + "\n\n")
    return redirect("/")

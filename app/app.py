from flask import Flask, request, abort, redirect, render_template
import flask
import os
import sys
import re
import time
import json
import better_random as random

import illumi
import anicat
import space
import status
from content_type import *
from subpages import *

app = Flask(__name__, template_folder = "../")

app.register_blueprint(illumi.blueprint)
app.register_blueprint(anicat.blueprint)
app.register_blueprint(space.blueprint)
app.register_blueprint(status.blueprint)

@app.route("/")
def index():
    with open("musiclist.jsonc", "r") as l:
        json_data = l.read()
        json_data = re.sub(r"/\*[\w ]*\*/", "", json_data) #清除注释
        lis = json.loads(json_data)
        url = random.choice(lis)
    return render_template("index.html",
        music_url = url,
        menu = menu)

@app.route("/<file>")
def file(file):
    if os.path.isfile(file) == False:
        abort(404)
    if file == "index.html":
        return redirect("/")
    if file.split(".")[-1] == "html":
        return render_template(file,
        menu = menu)
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

@app.route("/version")
def version():
    with open("version.html", "r") as f:
        data = f.read()
        data = data.replace("{py_version}", sys.version)
        data = data.replace("{flask_version}", flask.__version__)
    return data

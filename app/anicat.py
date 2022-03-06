from flask import Blueprint, abort
import os

blueprint = Blueprint("anict", __name__)
@blueprint.route("/anicat")
def illumi_index():
    if os.path.isfile("anicat/index.html") == False:
        abort(404)
    with open("anicat/index.html", "r") as f:
        return f.read()
@blueprint.route("/anicat/<file>")
def illumi(file):
    if os.path.isfile(f"anicat/{file}") == False:
        abort(404)
    with open(f"anicat/{file}", "r") as f:
        return f.read()
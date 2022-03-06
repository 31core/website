from flask import Blueprint, abort
import os

blueprint = Blueprint("illumi", __name__)
@blueprint.route("/illumi")
def illumi_index():
    if os.path.isfile("illumi/index.html") == False:
        abort(404)
    with open("illumi/index.html", "r") as f:
        return f.read()
@blueprint.route("/illumi/<file>")
def illumi(file):
    if os.path.isfile(f"illumi/{file}") == False:
        abort(404)
    with open(f"illumi/{file}", "r") as f:
        return f.read()
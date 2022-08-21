from flask import Blueprint, render_template
import os, sys

blueprint = Blueprint("status", __name__)
@blueprint.route("/status")
def get_status():
    return render_template("status.html", uname = os.popen("uname").read(),
        kernel_release = os.popen("uname -r").read(),
        arch = os.popen("uname -m").read())

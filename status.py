from flask import Blueprint, abort
import os, sys

def py_version(src):
    src = src.replace("{py_version}", sys.version)
    return src

blueprint = Blueprint("status", __name__)
@blueprint.route("/status")
def get_status():
    with open("status.html", "r") as f:
        html = f.read()
        html = html.replace("{uname}", os.popen("uname -a").read().replace("\n", "<br>").replace(" ", "&nbsp;"))
        html = html.replace("{cpu}", os.popen("lscpu").read().replace("\n", "<br>").replace(" ", "&nbsp;"))
        html = html.replace("{free}", os.popen("free -h").read().replace("\n", "<br>").replace(" ", "&nbsp;"))
        html = html.replace("{disk}", os.popen("df -h").read().replace("\n", "<br>").replace(" ", "&nbsp;"))
        html = html.replace("{uptime}", os.popen("uptime").read().replace("\n", "<br>").replace(" ", "&nbsp;"))
        html = py_version(html)
        return html

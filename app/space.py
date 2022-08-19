from flask import Blueprint, abort, render_template
import os

from subpages import *

blueprint = Blueprint("space", __name__)
@blueprint.route("/space")
def space_index():
    def get_time(name: str) -> str:
        """获取时间
        format: day-hour.min.sec~description"""
        name = name[:name.find("~")]
        name = name.replace("-", " ")
        name = name.replace(".", ":")
        return name
    def parse_content(con: str) -> str:
        con = con.replace("\n", "<br>")
        con = con.replace(" ", "&nbsp;")
        return con
    if os.path.isfile("space.html") == False:
        abort(404)
    subs = str()
    template = open("./subpages/space_sub.html").read() #读取模板
    for year in os.listdir("space"):
        for month in os.listdir(f"space/{year}"):
            for i in os.listdir(f"space/{year}/{month}"):
                with open(f"space/{year}/{month}/{i}") as sub:
                    subs += template.replace("{content}", parse_content(sub.read()))
                    subs = subs.replace("{date}", f"{year}-{month}-{get_time(i)}") #替换时间
    return render_template("space.html", menu = menu, 
        list = subs)

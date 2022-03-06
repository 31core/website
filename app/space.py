from flask import Blueprint, abort
import os

blueprint = Blueprint("space", __name__)
@blueprint.route("/space")
def space_index():
    def get_time(name: str):
        """获取时间"""
        name = name[:name.find("~")]
        name = name.replace("-", " ")
        name = name.replace(".", ":")
        return name
    def parse_content(con: str):
        con = con.replace("\n", "<br>")
        con = con.replace(" ", "&nbsp;")
        return con
    if os.path.isfile("space.html") == False:
        abort(404)
    with open("space.html", "r") as f:
        subs= str()
        template = open("space_sub.html").read() #读取模板
        for year in os.listdir("space"):
            for month in os.listdir(f"space/{year}"):
                for i in os.listdir(f"space/{year}/{month}"):
                    with open(f"space/{year}/{month}/{i}") as sub:
                        subs += template.replace("{content}", parse_content(sub.read()))
                        subs = subs.replace("{date}", f"{year}-{month}-{get_time(i)}") #替换时间
        return f.read().replace("{list}", subs)

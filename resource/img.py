from PIL import Image
import sys
import os
import json

def to_png(file):
    img = Image.new("RGBA", (32, 32))
    buffer = img.load()
    with open(file, "rb") as f:
        for y in range(32):
            for x in range(32):
                data = list(f.read(4))
                if data == b"":
                    break
                data.extend((4 - len(data)) * [0])
                buffer[x, y] = tuple(data)
    img.save("output.png")

def from_png(png):
    img = Image.open(png)
    buffer = img.load()
    with open("output", "wb") as f:
        for y in range(32):
            for x in range(32):
                f.write(bytes(buffer[x, y]))
    img.close()

if __name__ == "__main__":
    if sys.argv[1] == "--png":
        from_png(sys.argv[2])
    elif sys.argv[1] == "--file":
        if os.path.getsize(sys.argv[2]) <= 4 * 1024:
            to_png(sys.argv[2])
            with open("config.json", "w") as f:
                f.write(json.dumps({"name": os.path.basename(sys.argv[2]),\
                                    "size": os.path.getsize(sys.argv[2]),\
                                    "png-count": 1}))
        else:
            """文件大于4kb"""
            if os.path.isdir("output") == False:
                os.mkdir("output")
            num = os.path.getsize(sys.argv[2]) // (4 * 1024)
            if os.path.getsize(sys.argv[2]) % (4 * 1024) != 0:
                num += 1
            for i in range(num):
                # 分割文件
                with open(sys.argv[2], "rb") as f:
                    with open("part", "wb") as p:
                        f.seek(i * 4 * 1024)
                        p.write(f.read(4 * 1024))
                to_png("part")
                os.rename("output.png", f"output/part_{i}.png")
            os.remove("part")
            with open("output/config.json", "w") as f:
                f.write(json.dumps({"name": os.path.basename(sys.argv[2]),\
                                    "size": os.path.getsize(sys.argv[2]),\
                                    "png-count": num}))
    elif sys.argv[1] == "--config":
        os.chdir(os.path.abspath(os.path.dirname(sys.argv[2])))
        with open(sys.argv[2], "r") as f:
            config = json.loads(f.read())
        # 单文件
        if config.get("png-count") == 1:
            from_png("output.png")
            with open("output.f", "wb") as f:
                with open("output", "rb") as f1:
                    f.write(f1.read(config.get("size")))
            os.remove("output")
            os.rename("output.f", config.get("name"))
            exit()
        with open("output.f", "wb") as f:
            for i in range(config.get("png-count")):
                from_png(f"part_{i}.png")
                with open("output", "rb") as f1:
                    f.write(f1.read())
        # 还原文件大小
        with open("output", "wb") as f:
            with open("output.f", "rb") as f1:
                f.write(f1.read(config.get("size")))
        os.remove("output.f")
        os.rename("output", config.get("name"))

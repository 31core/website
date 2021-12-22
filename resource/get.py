from selenium import webdriver
from html.parser import HTMLParser
import urllib.request
from urllib.parse import urlparse
import os
import sys
from PIL import Image, ImageFile

img_list = []

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for (key, value) in attrs:
                if key == "data-src":
                    self.links.append(value)
                    if value.find("tn1.kkmh.com") == -1:
                        del self.links[-1]

def get_image(url):
    res = urllib.request.urlopen(url)
    with open(urlparse(url).path.split("/")[-1][:-2], "wb") as f:
        f.write(res.read())
    img_list.append(urlparse(url).path.split("/")[-1][:-2])

def image_contact(src, src2):
    img = Image.open(src)
    y = img.size[1]
    img2 = Image.open(src2)
    target = Image.new("RGB", (img2.size[0], y + img2.size[1]))
    target.paste(img, (0, 0))
    target.paste(img2, (0, y))
    target.save(src[:-3] + "png")

if __name__ == "__main__":
    os.chdir("cache")

    url = sys.argv[1]
    
    driver = webdriver.Firefox()
    driver.get(url)
    parser = MyHTMLParser()
    parser.feed(driver.page_source)
    driver.close()

    print("Downloading images...")
    pro = 1
    for i in parser.links:
        get_image(i)
        print("[%d%%] %s (%d of %d)"%((pro / len(parser.links) * 100), i, pro, len(parser.links)))
        pro += 1

    print("Contacting images...")
    pro = 1
    for i in img_list[1:]:
        image_contact(img_list[0], i)
        img_list[0] = img_list[0][:-3] + "png"
        print("[%d%%] %s (%d of %d)"%((pro / (len(img_list) - 1) * 100), i, pro, (len(img_list) - 1)))
        pro += 1
    os.rename(img_list[0][:-3] + "png", "../images/img.png")
        

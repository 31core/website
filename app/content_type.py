content_types = {
    "html": "text/html",
    "xml": "text/xml",
    "css": "text/css",
    "txt": "text/plain",
    "ico": "application/x-ico",
    "js": "application/x-javascript",
    "json": "application/json",
    "pdf": "application/pdf",
    "png": "image/png",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "webp": "image/webp",
    "gif": "image/gif",
    "mp4": "video/mpeg4",
    "mid": "audio/mid",
    "mp3": "audio/mp3",
    "wav": "audio/wav"
}

def content_type(name: str, charset = None) -> str:
    name = name.split(".")[-1]
    if name.lower() in content_types:
        if charset != None and\
            content_types[name.lower()].split("/")[0] == "text":
            return "%s; charset=%s"%(content_types[name.lower()], charset)
        return content_types[name.lower()]
    return "application/octet-stream"

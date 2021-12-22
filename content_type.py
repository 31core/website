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
    "gif": "image/gif",
    "mp4": "video/mpeg4",
    "mid": "audio/mid",
    "mp3": "audio/mp3",
    "wav": "audio/wav"
}

def content_type(name: str):
    name = name.split(".")[-1]
    if name.lower() in content_types:
        return content_types[name.lower()]
    return "application/octet-stream"
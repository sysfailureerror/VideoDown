#by SysFailureError
#date: 06/2020

from __future__ import unicode_literals
import youtube_dl

class YtLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

class Download(object):
    def __init__(self):
        self.ytdl_opts = {}
        self.url = ""
        self.ytdl_obj = None
    
    def init_ytdl(self):
        self.ytdl_obj = youtube_dl.YoutubeDL(self.ytdl_opts)
        return True

    def start(self):
        self.ytdl_obj.download([self.url])
        return True

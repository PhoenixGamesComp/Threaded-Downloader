import requests
from lxml.html import fromstring
from threading import Thread


class Downloader(Thread):

    def __init__(self, url, bytes, start, part):

        Thread.__init__(self)
        self.url = url
        self.bytes = bytes
        self.part = part

        end = start + bytes
        self.headers = {"Range": "bytes={}-{}".format(start, end)}

    def download(self):

        self.r = requests.get(self.url, headers=self.headers, allow_redirects=True, stream=True)
        name = "./temp/part{}".format(self.part)

        with open(name, 'wb') as f:

            f.write(self.r.content)

    def run(self):

        self.download()
        

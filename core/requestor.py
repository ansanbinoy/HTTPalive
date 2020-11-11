import requests, os, sys, argparse, re
from threading import Thread
from core.color import error, red, reset
global list
class Req(Thread):
        def __init__(self,url,file):
                Thread.__init__(self)
                self.url = url.split("\n")[0]
                self.file = file
                if not self.url.startswith("https://"):
                        self.url = "https://"+self.url
                else:
                        self.url = self.url
        def run(self):
                list = []
                try:
                        x = requests.get(self.url,timeout=1001)
                        resp = self.url+"  \t  "+str(x.status_code)

                        print (resp)
                        list.append(resp)
                except:
#                        print (error+red+self.url+"\tFailed to connect!."+reset)
                        pass
def launch(urls,th,file=None):
        for i in range(len(urls)):
                if 1 < 100:
                        url = urls.pop(0)
                        thread = Req(url,file)
                        thread.start()
        for i in range(int(th)):
                thread.join()

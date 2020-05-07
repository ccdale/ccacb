#!/usr/bin/env python3
"""Watches the system clipboard for youtube urls"""
import os
import pyperclip
from pyperclip import waitForNewPaste
import queue
import subprocess
import threading
import time


def getUrl(url):
    os.chdir("/home/chris/Videos/kmedia/incoming")
    cmd = ["/home/chris/bin/youtube-dl", url]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

def doYouTube(Q):
    try:
        while True:
            if Q.empty():
                time.sleep(1)
            else:
                iurl = Q.get()
                if iurl == "STOP":
                    break
                tmp = iurl.split("&")
                url = tmp[0]
                print(url)
                getUrl(url)

def goBabe():
    """youtube urls look like

    https://www.youtube.com/watch?v=hMk6rF4Tzsg
    https://www.youtube.com/watch?v=pL3Yzjk5R4M&list=RDCMUCmM3eCpmWKLJj2PDW_jdGkg&start_radio=1&t=8
    """
    Q = queue.Queue()
    try:
        thread = threading.Thread(target=doYouTube, args=[Q])
        thread.start()
        while True:
            txt = waitForNewPaste()
            if txt.startswith("https://www.youtube.com/watch"):
                Q.put(txt)
    except KeyboardInterrupt:
        print("Will finish off the Q, then exit")
        Q.put("STOP")
        thread.join()
        print("Q has completed")


if __name__ == "__main__":
    goBabe()

#!/usr/bin/env python3
"""Watches the system clipboard for youtube urls"""
import ccalogging
import os
import pyperclip
from pyperclip import waitForNewPaste
import queue
import subprocess
import threading
import time
import sys

import ccacb

ccalogging.setConsoleOut()
ccalogging.setInfo()
log = ccalogging.log


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
    except Exception as e:
        log.error(f"Exception in doYouTube: {e}")
        sys.exit(1)


def goBabe():
    """youtube urls look like

    https://www.youtube.com/watch?v=hMk6rF4Tzsg
    https://www.youtube.com/watch?v=pL3Yzjk5R4M&list=RDCMUCmM3eCpmWKLJj2PDW_jdGkg&start_radio=1&t=8
    """
    log.info(f"ccacb - youtube-dl clipboard queue processor {ccacb.__version__}")
    Q = queue.Queue()
    thread = threading.Thread(target=doYouTube, args=[Q])
    thread.start()
    try:
        while True:
            txt = waitForNewPaste()
            if txt.startswith("https://www.youtube.com/watch"):
                Q.put(txt)
    except KeyboardInterrupt:
        log.info("Interrupted: Will finish off the Q, then exit")
    Q.put("STOP")
    thread.join()
    log.info("ccacb has finished")


if __name__ == "__main__":
    goBabe()

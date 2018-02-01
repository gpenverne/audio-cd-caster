#!/usr/bin/env python3

import subprocess
import time
import os
import pygame
import datetime
import argparse
import pychromecast
import json
import requests

class Launcher():
    def __init__(self,cdDrive):
        self.cdDrive = cdDrive
        self.cdDrive.init()
        self.currentPath = os.path.dirname(os.path.realpath(__file__))
        configFile = self.currentPath + "/config.json"
        self.config = json.loads(open(configFile, 'r').read())

    def start(self):
        subprocess.call(["eject"])
        while True:
            if self.cdDrive.get_empty() == False:
                if self.cdDrive.get_track_audio(0) == True:
                    ripit = subprocess.Popen(self.currentPath+"/play.sh", shell=True)
                    chromecasts = pychromecast.get_chromecasts()
                    cast = next(cc for cc in chromecasts if cc.device.friendly_name == self.config['chromecast_friendly_name'])
                    open("/tmp/acdcaster.pid", 'a').close()
                    self.playToChromecast(cast)

            time.sleep(1)

    def playToChromecast(self, cast):
        for subdir, dirs, files in os.walk(self.currentPath):
            for file in files:
                 filepath = subdir + os.sep + file
                 if filepath.endswith('.wav'):
                     cast.wait()
                     mc = cast.media_controller
                     url=self.config['public_url_prefix']+str(time.time())+".wav"
                     print("Waiting for server ready")
                     requests.get(self.config['public_url_prefix']+'status')
                     print("Chromecast is launching")
                     mc.play_media(url, "audio/wav", "CD Audio")
                     print("Chromecast is playing")
                     while not self.cdDrive.get_empty() and os.path.exists("/tmp/acdcaster.pid") and os.path.exists(filepath):
                         echo "Waiting for end"
                         time.sleep(1)
                         continue
                     print("Stopping")
                     ripit = subprocess.Popen(self.currentPath+"/stop.sh", shell=True)
                     os.path.remove(filepath)
                     mc.stop()
                     break

if __name__ == "__main__":
    pygame.cdrom.init()
    launcher = Launcher(pygame.cdrom.CD(0))
    launcher.start()
    pygame.cdrom.quit()

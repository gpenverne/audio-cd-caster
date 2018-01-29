#!/usr/bin/env python

import subprocess
import time
import os
import pygame
import datetime
import argparse
import pychromecast
import json

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
                    while os.path.exists("/tmp/acdcaster.pid"):
                        self.playToChromecast(cast)
                        time.sleep(1)
                        continue

            time.sleep(1)

    def playToChromecast(self, cast):
        for subdir, dirs, files in os.walk(self.currentPath):
            for file in files:
                 filepath = subdir + os.sep + file
                 if filepath.endswith('.wav'):
                     cast.wait()
                     mc = cast.media_controller
                     url=self.config['public_url_prefix']+str(time.time())+".wav"
                     mc.play_media(url, "audio/wav", "CD Audio")
                     while mc.status.is_playing:
                         time.sleep(1)
                         continue

if __name__ == "__main__":
    pygame.cdrom.init()
    launcher = Launcher(pygame.cdrom.CD(0))
    launcher.start()
    pygame.cdrom.quit()

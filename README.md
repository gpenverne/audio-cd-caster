# Audio-cd-caster

Play audio cd to chromecast

Thanks to:
    - [https://github.com/martinohanlon/AutoRipper](https://github.com/martinohanlon/AutoRipper)
    - [https://github.com/balloob/pychromecast](https://github.com/balloob/pychromecast)

## Setup

Requirements:

- python3
- nodejs
- abcde
- pygame for python3


```shell
npm install
sudo apt-get build-dep python-pygame
pip3 install -r requirements.txt
sudo apt-get install abcde
sudo cp 99-play-disc-to-chrome-cast.rules /etc/udev/rules.d/99-play-disc-to-chrome-cast.rules
sudo udevadm control --reload
cp config.json.dist config.json
```

## Configuration

Edit ``config.json`` file:

- ``chromecast_friendly_name``: target chromecast to play audio
- ``public_url_prefix``: the public url of the server.js server (needed by chromecast)


## Start it!

Launch launcher.py:

```shell
python3 launcher.py
```

## Start it at start!
```shell
crontab -e
```

Add this line to your crontab:
```
@reboot python /home/pi/mp3/laucher.py > /tmp/rip.log
```

## Details

``server.js`` will serve a fake big wav file. Chromecast will stream it.

``launcher.py`` will check if audio cd is here. If audio cd is ready, it launches the ``play.sh`` script, and look for wav file. If wav file found, it launches it on chromecast

``play.sh`` will launch the nodejs server, and abcde to rip the disc, and writes pid files

``stop.sh`` will kill abcde and server.js

``99-play-disc-to-chrome-cast.rules`` will launch the ``stop.sh`` when the disc is removed

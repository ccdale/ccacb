# ytcb
Watches the clipboard for youtube urls and downloads them.

Will now auto-update youtube-dl on startup

## install

from pypi:

```
python3 -m pip install ccacb --user --upgrade
```

from the repo (requires poetry):
```
git clone https://github.com/ccdale/ccacb.git
cd ccacb
poetry install
poetry build
python3 -m pip install dist/ccacb-0.6.6-py3-none-any.whl --user --upgrade
```

## config
edit `~/.config/ytcb.yaml`

```
---
youtubedl: /home/chris/bin/youtube-dl
incoming: /home/chris/Videos
```

## example

```
$ ytcb
08/05/2020 13:47:55 [INFO ]  ytcb - youtube-dl clipboard queue processor 0.6.3
08/05/2020 13:47:55 [INFO ]  reading /home/chris/.config/ytcb.yaml
08/05/2020 13:47:55 [INFO ]  Using /home/chris/bin/youtube-dl
08/05/2020 13:47:55 [INFO ]  youtube-dl will store files in /home/chris/Videos/kmedia/incoming

<CTRL>-c

08/05/2020 13:48:11 [INFO ]  Interrupted: Will finish off the Q, then exit
08/05/2020 13:48:12 [INFO ]  ytcb has finished
```

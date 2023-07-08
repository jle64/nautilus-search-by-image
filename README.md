# Reverse image search for Nautilus

Nautilus plugin that adds contextual menu entries on image files to do a reverse image search on them using Google or Yandex.

![Sreencapture](screencapture.png)

## Installation

### Arch Linux

Install `nautilus-search-by-image-git` from AUR.

### Manual

Install the `python-nautilus` or `nautilus-python` and `python-requests` or `python3-requests` packages depending on your distro.

Place the search-by-image.py file in the nautilus-python user or system directory and restart Nautilus.

For example, to place it in the user directory (usually `~/.local/share/nautilus-python/extensions`, unless overriden by XDG env var):
```shell
git clone https://github.com/jle64/nautilus-search-by-image && cd nautilus-search-by-image
install -D search-by-image.py "${XDG_DATA_HOME-${HOME}/.local/share}/nautilus-python/extensions/search-by-image.py"
nautilus -q
```

## Privacy caveats

When doing a search, your image is uploaded to a file sharing service, in addition to the search engine, so this file sharing service also gets to access the image you're searching.
This is done because it's easier to do a reverse image search on a Web file rather than a local one.
By default the service used is <https://transfer.sh>, it be changed by editing the `UPLOAD_URL` variable.

## Troubleshooting

In case of issue, either try to look at your logs (`journalctl --user` on systemd-based systems) or run nautilus in a terminal after killing it (`nautilus -q; nautilus`) and see if there is anything relevant.

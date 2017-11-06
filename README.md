# Reverse Google image search for Nautilus

Simple Nautilus plugin to open a reverse Google image search page in the default browser through the contextual menu (adds a "Search image on Google" entry in contextual menu on image files).

## Installation

### Arch Linux

Install `nautilus-search-by-image-git` from AUR.

### Manual

Install `python2-nautilus` and `python2-requests` packages (`python-nautilus` and `python-requests` on some distribs).

Place the google-image.py file in the nautilus-python user or system directory and restart Nautilus.

For example, to place it in the user directory:
```shell
EXTDIR="${XDG_DATA_HOME-${HOME}/.local/share}/nautilus-python/extensions"
mkdir -p "${EXTDIR}"
cp google-image.py "${EXTDIR}"/google-image.py
nautilus -q
```

## Caveats

When doing a search, your image is uploaded to a file sharing service (defaults to transfer.sh, can be changed by editing the `UPLOAD_URL` variable), so in addition to Google this file sharing service also gets to access the image you're searching.
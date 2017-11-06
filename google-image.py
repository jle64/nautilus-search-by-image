# -*- coding: UTF-8 -*-
import requests
from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject, Gio

SEARCH_URL = 'https://www.google.com/searchbyimage?&image_url='
UPLOAD_URL = 'https://transfer.sh/image'

class GoogleImageExtension(GObject.GObject, Nautilus.MenuProvider):
    def _google_image(self, menu, nfile):
        # Get Gio.File from NautilusVFSFile
        gfile = Gio.File.new_for_uri(nfile.get_uri())
        with open(gfile.get_path(), 'r') as content_file:
            content = content_file.read()

        r = requests.put(UPLOAD_URL, data=content)
        if r.status_code != 200:
            return

        uploaded_url = r.text.strip()
        Gio.AppInfo.launch_default_for_uri(SEARCH_URL + uploaded_url, None)

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        nfile = files[0]

        if nfile.is_directory():
            return

        if nfile.get_mime_type().split('/')[0] != 'image':
            return

        item = Nautilus.MenuItem(
            name='NautilusPython::google_image_search_file_item',
            label='Search image on Google',
            tip='Use Google reverse image search on %s' % nfile.get_name()
        )
        item.connect('activate', self._google_image, nfile)

        return [item]

    def get_background_items(self, window, nfile):
        return

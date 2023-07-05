import sys
import requests
import gi

gi.require_version("Gio", "2.0")
gi.require_version("GObject", "2.0")
from gi.repository import GObject, Gio

from gi.repository import Nautilus

SEARCH_URLS = {
    "Yandex": "https://yandex.com/images/search?rpt=imageview&url=",
    "Google": "https://lens.google.com/uploadbyurl?url="
}
UPLOAD_URL = "https://transfer.sh/image"


class SearchByImageExtension(GObject.GObject, Nautilus.MenuProvider):
    def _search_image(self, menu, nfile, engine):
        # Get Gio.File from NautilusVFSFile
        gfile = Gio.File.new_for_uri(nfile.get_uri())
        with open(gfile.get_path(), "rb") as content_file:
            content = content_file.read()

        r = requests.put(UPLOAD_URL, data=content)
        if r.status_code != 200:
            return

        uploaded_url = r.text.strip()
        Gio.AppInfo.launch_default_for_uri(SEARCH_URLS[engine] + uploaded_url, None)

    def get_file_items(self, files):
        if len(files) != 1:
            return

        nfile = files[0]

        if nfile.is_directory():
            return

        if nfile.get_mime_type().split("/")[0] != "image":
            return

        menu = Nautilus.MenuItem(
            name="SearchByImageExtension::Engines", label="Search by image"
        )

        submenu = Nautilus.Menu()
        menu.set_submenu(submenu)
        for engine in SEARCH_URLS.keys():
            item = Nautilus.MenuItem(
                name=f"SearchByImageExtension::{engine}",
                label=f"Search image on {engine}",
                tip=f"Use {engine} reverse image search on {nfile.get_name()}",
            )
            item.connect("activate", self._search_image, nfile, engine)
            submenu.append_item(item)

        return (menu,)

    def get_background_items(self, nfile):
        return

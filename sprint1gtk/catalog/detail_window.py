import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SubWindow(Gtk.Window):


    def __init__(self, name, image, descripcion):
        super().__init__(title=name)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(image, True, True, 0)
        box.pack_start(Gtk.Label(descripcion), True, True, 0)
        self.add(box)
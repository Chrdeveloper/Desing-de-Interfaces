import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf

class SubWindow(Gtk.Window):
    name = None
    descripcion = None
    image = Gtk.Image()

    def __init__(self, name, image, descripcion):
        super().__init__(title=name)
        self.name = name
        self.descripcion = descripcion
        self.image = image
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(self.image, True, True, 0)
        box.pack_start(Gtk.Label(self.descripcion), True, True, 0)
        self.add(box)
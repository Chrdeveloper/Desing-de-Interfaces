import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SubWindow(Gtk.Window):
    def __init__(self,imageM, imageJ):
        super().__init__(title="Resultado")

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box.pack_start(imageJ, True, True, 0)
        box.pack_start(imageM, True, True, 0)
        self.add(box)
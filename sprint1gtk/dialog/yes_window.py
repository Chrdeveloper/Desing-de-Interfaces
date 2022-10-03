import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SiWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Si")
        label = Gtk.Label("Maria2")
        self.add(label)

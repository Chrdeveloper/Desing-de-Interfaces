import gi
import self

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class NoWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="No")
        label = Gtk.Label("Maria")
        self.add(label)


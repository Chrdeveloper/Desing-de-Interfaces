import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

Window = Gtk.Window(title="Hello World")
Window.show()
Window.connect("destroy", Gtk.main_quit)
Gtk.main()

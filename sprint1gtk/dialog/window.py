import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from yes_window import SiWindow

from no_window import NoWindow

class MainWindow(Gtk.Window):
    buttonNo = Gtk.Button(label="No")
    buttonSi = Gtk.Button(label="Si")
    label = Gtk.Label("Funciona profavor")
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)
        self.add(self.box)

        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.box2, True, True, 0)

        self.buttonSi.connect("clicked", self.on_buttonSi_clicked)
        self.box2.pack_start(self.buttonSi, True, True, 0)

        self.buttonNo.connect("clicked", self.on_buttonNo_clicked)
        self.box2.pack_start(self.buttonNo, True, True, 0)

    def on_buttonSi_clicked(self, widget):
        win = SiWindow()
        win.show_all()



    def on_buttonNo_clicked(self, widget):
        win = NoWindow()
        win.show_all()

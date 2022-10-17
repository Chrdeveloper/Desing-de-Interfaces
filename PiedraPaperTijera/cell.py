import random


import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from SubWindow import SubWindow
class Cell(Gtk.EventBox):
    name = None
    image = Gtk.Image()

    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image = image

        box = Gtk.Box(orientation= Gtk.Orientation.VERTICAL, spacing=4 )
        box.pack_start(Gtk.Label(label = name), False, False, 0)
        box.pack_start(self.image, True, True, 0)

        self.add(box)
        self.connect("button-release-event", self.on_click)

    def eleccionMaquina(self):
        rand = None
        pixbuf =  None
        rand = random.randint(1,3)
        if(rand == 1):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("images/tijeras.jpg",200,200, False)
        elif(rand == 2):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("images/piedra.jpg",200,200, False)
        elif(rand == 3):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("images/piedra.jpg",200,200, False)

        return pixbuf



    def on_click(self,widget,event):
        imageNew = Gtk.Image()
        imageJ = Gtk.Image()
        pixbuff = None
        pixbuff = self.eleccionMaquina()
        imageNew.set_from_pixbuf(pixbuff)


        imageJ.set_from_pixbuf(self.image.get_pixbuf())

        win = SubWindow(imageNew, imageJ)
        win.show_all()
        Gtk.main()
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SubWindow(Gtk.Window):#Decimos que tipo de gtk es


    def __init__(self, name, image, descripcion):
        super().__init__(title=name)#Llamamos al constructor y le damos el titulo en el name
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)#Creamos la box
        box.pack_start(image, True, True, 0)#Añadimos imagen
        self.set_position(Gtk.WindowPosition.CENTER)
        box.pack_start(Gtk.Label(descripcion), True, True, 0)#Añadimos texto
        self.add(box)#añadimos la box a la interface
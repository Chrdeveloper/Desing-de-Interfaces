import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class MainWindow(Gtk.Window):
    lista = ["casa", "cerdo", "portatil", "cuchara", "trompeta", "desayuno"]
    fallos = 0
    letra = ""
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
    entry = Gtk.Entry()
    esperando = True
    position = 0

    def __init__(self, listaObj):
        super().__init__()
        gword = Gtk.Label(self.palabra_adivinar())
        boton = Gtk.Button()
        boton.connect("clicked", self.clicked)

        while self.fallos < 6:
            self.box.pack_start(gword, True, True, 0)
            self.box.pack_start(self.genImg(listaObj), True, True, 0)

            self.box.pack_start(self.entry, True, True, 0)

            self.box.pack_start(boton, True, True, 0)

            self.add(self.box)
            if self.esperando == False:
                if self.letra_igual() != -1:
                    self.position = self.letra_igual()
                    gword = self.palabra_modificada(gword, self.position)
                    self.esperando = True

            self.remove(self.box)

    def letra_igual(self):
        position = 0
        for letter in self.lista[0]:
            if letter == self.letra:
                return position
            position += 1
        self.fallos += 1
        return -1

    def palabra_adivinar(self):
        palabra = ''
        for i in range(len(self.lista[1])):
            palabra += '_'
        return palabra

    def palabra_modificada(self, gword, posicion):
        palabra = ''
        position = 0
        for letter in gword:
            if letter == '_':
                if self.position == posicion:
                    palabra += self.letra
            else:
                palabra += '_'
            position += 1

        return palabra

    def genImg(self, listaObj):
        img = Gtk.Image()
        for item in listaObj:
            if item.get("fallos") == self.fallos:
                img = item.get("gtk image")
        return img

    def clicked(self, event):
        self.esperando = False
        self.letra = self.entry.get_text()

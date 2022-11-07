import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class MainWindow(Gtk.Window):
    lista = ["casa", "cerdo", "portatil", "cuchara", "trompeta", "desayuno"]

    fallos = 0

    label = Gtk.Label

    img = Gtk.Image
    boton = Gtk.Button()
    entry = Gtk.Entry()
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    def __init__(self, listaObj):
        super().__init__()

        self.label = self.palabra_adivinar()

        self.img = self.genImg(listaObj)

        self.boton.connect("clicked", self.onClick, listaObj)

        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.img, True, True, 0)
        self.box.pack_start(self.entry, True, True, 0)
        self.box.pack_start(self.boton, True, True, 0)

        self.add(self.box)

    def letra_igual(self, letra, aux):
        position = 0
        letraMet = letra
        for letter in self.lista[0]:
            if letter == letraMet:
                if aux[position] == '_':
                    return position
            position += 1
        self.fallos += 1
        return -1

    def palabra_adivinar(self):
        palabra = ''
        for i in range(len(self.lista[1])):
            palabra += '_'
        return Gtk.Label(palabra)

    def palabra_modificada(self, gword, posicion, text):
        palabra = ''
        position = 0
        for letter in gword:

            if position == posicion:
                palabra += text
            else:
                palabra += gword[position]

            position += 1

        return palabra

    def genImg(self, listaObj):
        img = Gtk.Image()
        for item in listaObj:
            if item.get("fallos") == self.fallos:
                img = item.get("gtk image")
        return img

    def onClick(self,event, listaObj):



        text = self.entry.get_text()

        #Algunos metodos nos pediran texto y no una Label, por lo que generamos texto de la label mediante el siguiente metodo y lo metemos en una variable
        aux = self.label.get_text()

        acierto = self.letra_igual(text,aux)
        if acierto != -1:

            self.label.set_label(self.palabra_modificada(aux, acierto, text))
        else:
            self.fallos += 1
            self.img = self.genImg(listaObj)

        self.modificador()
        self.actualizador(listaObj)

    def modificador(self):
        self.box.remove(self.label)
        self.box.remove(self.img)
        self.box.remove(self.entry)
        self.box.remove(self.boton)

        self.remove(self.box)

    def actualizador(self,listaObj):

        self.box.pack_start(self.label, True, True, 0)
        self.img.set_from_pixbuf(self.genImg(listaObj).get_pixbuf())
        self.box.pack_start(self.img, True, True, 50)
        self.box.pack_start(self.entry, True, True, 0)
        self.box.pack_start(self.boton, True, True, 0)

        self.add(self.box)

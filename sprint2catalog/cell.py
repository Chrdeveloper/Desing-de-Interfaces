import gi
from gi.repository import GdkPixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import SubWindow


class Cell(Gtk.EventBox):#Decimos que tipo de clase es
    name = None#Declaramos variables de clase...
    image = Gtk.Image()


    def __init__(self, name, description, image):
        super().__init__()#Llamamos al superconstructor
        self.description = description

        self.name = name#El name tendra el valor name asignado en el consctructor y que se le otorga cuando llaman al metodo
        self.image = image#La image tendra el valor image asignado al igual que en name por el metodo que lo llama
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)#creamos y signamos  e identacion en la presentacion en la box
        box.pack_start(Gtk.Label(label=name), False, False, 0)#Añadimos el label que es la imagen en la box
        box.pack_start(self.image, True, True, 0)#Añadimos la imagen en el box
        self.add(box)#Añadimos la box con el contenido añadido previamente
        self.connect("button-release-event", self.on_click) #Conectamos el evento de pulsar una imagen usando on_click

    def on_click(self, widget, event):#Debemos pasarle el evento(asignado en el connect) y el widget que es la propia cell
        im = Gtk.Image() #Debido al como implementa gtk los widget tenemos que reasignarle otra imagen(aunque sea la misma) a la imagen gtk, por ello en este metodo segun el name reasignamos la variable imagen
        im.set_from_pixbuf(self.image.get_pixbuf())
        win = SubWindow(self.name, self.image, self.descripcion) #Le damos al constructor de la siguiente clase el nombre, la imagen y descripcion
        win.show_all()#Mostramos la pantalla con la imagen y su descripcion
        Gtk.main()

import gi
from gi.repository import GdkPixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import SubWindow


class Cell(Gtk.EventBox):#Decimos que tipo de clase es
    name = None#Declaramos variables de clase...
    descripcion = None
    image = Gtk.Image()


    def __init__(self, name, image):
        super().__init__()#Llamamos al superconstructor
        self.name = name#El name tendra el valor name asignado en el consctructor y que se le otorga cuando llaman al metodo
        self.image = image#La image tendra el valor image asignado al igual que en name por el metodo que lo llama
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)#creamos y signamos  e identacion en la presentacion en la box
        box.pack_start(Gtk.Label(label=name), False, False, 0)#Añadimos el label que es la imagen en la box
        box.pack_start(self.image, True, True, 0)#Añadimos la imagen en el box
        self.add(box)#Añadimos la box con el contenido añadido previamente
        self.connect("button-release-event", self.on_click) #Conectamos el evento de pulsar una imagen usando on_click

    def on_click(self, widget, event):#Debemos pasarle el evento(asignado en el connect) y el widget que es la propia cell
        self.image = self.getImage() #Debido al como implementa gtk los widget tenemos que reasignarle otra imagen(aunque sea la misma) a la imagen gtk, por ello en este metodo segun el name reasignamos la variable imagen
        self.annadir_descr() #Asigna a la variable de clase descripcion, una descripcion que concuerde con la imagen
        win = SubWindow(self.name, self.image, self.descripcion) #Le damos al constructor de la siguiente clase el nombre, la imagen y descripcion
        win.show_all()#Mostramos la pantalla con la imagen y su descripcion
        Gtk.main()

    def annadir_descr(self):

        if self.name == "Corki actimel":
            self.descripcion = "Corki actimel es una skin legendaria, que nos recuerda a todos la necesidad de tomar actimel para estar sanos, no disponible actualmente"
        elif self.name == "Robot volador":
            self.descripcion = "Mi campeón favorito, sin duda alguna Anivia, la criofenix. No tendrá mucho ataque, no tendrá mucha defensa... pero me encanta. Es muy difícil de controlar, sobre todo la Q, porque tienes que petarla y controlar la distancia muy bien para stunear. Mi campeón favorito, sin duda alguna Anivia, la criofenix."
        elif self.name == "Chogath caballero":
            self.descripcion = "Leí que jugar chogath caballero trae una notable mejora en el léxico. Me quedé absorto ante tal afirmación carente de raciocinio. Me exacerba cuando de soslayo, un petulante enarbola cultismos de rimbombantes como banales corolarios cuyo efímero fin es jugar chogath"
        elif self.name == "Gragas campesino":
            self.descripcion = "El famoso gragas gallego, debido a sus capacidades como el levantamiento de vacas y la capacidad de beber cerveza fue nombrado gallego del año"
        elif self.name == "Malphite whasap":
            self.descripcion = "Debido al increible aumento de la popularidad del lol, whasap no perdio el tiempo y quiso sacar una skin colaborando con riot games"
    def getImage(self):
        img = Gtk.Image()
        if self.name == "Corki actimel":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Corki.jpg", 200, 200, False)
        elif self.name == "Robot volador":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Anivia.png", 200, 200, False)
        elif self.name == "Chogath caballero":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Chogath.jpg", 200, 200, False)
        elif self.name == "Gragas campesino":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Gragas.jpg", 200, 200, False)
        elif self.name == "Malphite whasap":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Malphite.jpg", 200, 200, False)

        img.set_from_pixbuf(pixbuf)
        return img
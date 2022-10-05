import gi
from gi.overrides import GdkPixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import SubWindow


class Cell(Gtk.EventBox):
    name = None
    descripcion = None
    image = Gtk.Image()


    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image = image
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(self.image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)

    def on_click(self, widget, event):
        self.image = self.getImage()
        self.annadir_descr()
        win = SubWindow(self.name, self.image, self.descripcion)
        win.show_all()
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
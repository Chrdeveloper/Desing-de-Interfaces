import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from cell import Cell


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self, data_source):
        super().__init__(title="Catalogo")  # Asignamos el titulo de la ventana
        self.connect("destroy", Gtk.main_quit)  # Aseguramos que se cierre en la x
        self.set_border_width(15)  # Asignamos el borde que queramos
        self.set_default_size(400, 400)  # Asignamos el tamaño de la pantañña

        # Crearemos una gtk.HeaderBar donde personalizaremos el header de la ventana
        header = Gtk.HeaderBar(title="Skins")  # Asignamos el nombre del header
        header.set_subtitle("Las mejores skins")  # Asignamos el subtitulo
        header.props.show_close_button = True  # Le decimos que muestre la X de la ventana

        self.set_titlebar(header)  # Le asignaremos el header nuestro a la ventana

        # Le ponemos la rueda para subir y bajar en la pantalla
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)  # Lo añadimos a la flowbox
        self.add(scrolled)  # Añadimos la barra de scroll a la interfaz.

        image = Gtk.Image()  # Declaramos una variable Gtk.Image al cual le daremos una imagen
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Corki.jpg", 200, 200,
                                                         False)  # Crea un pixbuf exacto con las medidas y el archivo pasado como parametro
        image.set_from_pixbuf(pixbuf)  # Asignamos la imagen del pixbuf a la variable imagen
        cell_one = Cell("Corki actimel",
                        image)  # Llamamos al constructor cell y le damos nombre e imagen para que asigne las acciones correspondientes de la celda

        image2 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Anivia.png", 200, 200, False)
        image2.set_from_pixbuf(pixbuf)
        cell_two = Cell("Robot volador", image2)

        image3 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Chogath.jpg", 200, 200, False)
        image3.set_from_pixbuf(pixbuf)
        cell_three = Cell("Chogath caballero", image3)

        image4 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Gragas.jpg", 200, 200, False)
        image4.set_from_pixbuf(pixbuf)
        cell_four = Cell("Gragas campesino", image4)

        image5 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Malphite.jpg", 200, 200, False)
        image5.set_from_pixbuf(pixbuf)
        cell_five = Cell("Malphite whasap", image5)

        self.flowbox.add(cell_one)  # Añadimos a la flowbox las celdas
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)

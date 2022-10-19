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
        self.set_position(Gtk.WindowPosition.CENTER)
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

        for item in data_source:
            cell = Cell(item.get("name"),item.get("description"),item.get("gtk image"))
            self.flowbox.add(cell)
import gi
import gtk

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

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

        # Declaramos el menu de la barra, a este le añadimos las 2 opciones en forma de muñeca rusa

        menu_bar = Gtk.MenuBar()
        # Creamos la opcion que despliega el menu
        filemenu = Gtk.Menu()
        filem = Gtk.MenuItem("Ayuda")
        filem.set_submenu(filemenu)
        # Añadimos la primera opcion del menu y la anidamos al filemenu creado
        option1 = Gtk.MenuItem("Acerca de")
        option1.connect("activate", self.click)
        filemenu.append(option1)

        menu_bar.append(filem)

        # Añadimos a la vbox el scrolled anterior y el propio menu_bar
        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(menu_bar, False, False, 0)
        vbox.pack_start(scrolled, True, True, 0)
        self.add(vbox)

        for item in data_source:
            cell = Cell(item.get("name"), item.get("description"), item.get("gtk image"))
            self.flowbox.add(cell)

    # Definimos la accion que ocurre al pulsar el boton
    def click(self, event):
        win = Gtk.Window(title="Hecho por Christian Martinez!")
        label = Gtk.Label("Hecho por Christian Martinez")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(label, True, True, 0)
        win.add(box)
        win.show_all()

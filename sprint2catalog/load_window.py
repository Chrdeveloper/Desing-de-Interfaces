import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class LoadWindow(Gtk.Window):
    label = Gtk.Label("Cargando elementos...")
    spinner = Gtk.Spinner()#Declaramos el spinner
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 20)
    
    def __init__(self):
        super().__init__(title=' ')

        self.connect("destroy", Gtk.main_quit)#Permitimos cerrar la pantalla
        self.set_border_width(50)
        self.set_resizable(False)#No dejamos que cambie el tamaño de la ventana

        self.spinner.props.active = True#Dejamos que vaya dando vuelvas

        #Añdimos los elementos a la box
        self.box.pack_start(self.label,False, False,0)
        self.box.pack_start(self.spinner,False, False, 0)
        self.add(self.box)

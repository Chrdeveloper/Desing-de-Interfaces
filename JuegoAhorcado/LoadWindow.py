import shutil
import threading

import gi
import requests
from gi.overrides import GLib

gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from MainWindow import MainWindow

class LoadWindow(Gtk.Window):
    label = Gtk.Label("Cargando elementos")
    spinner = Gtk.Spinner()
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)


    def __init__(self):
        super().__init__()
        self.connect("destroy", Gtk.main_quit)  # Permitimos cerrar la pantalla
        self.set_border_width(50)
        self.set_resizable(False)  # No dejamos que cambie el tamaño de la ventana
        self.set_position(Gtk.WindowPosition.CENTER)
        self.spinner.props.active = True  # Dejamos que vaya dando vuelvas

        # Añdimos los elementos a la box
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)
        self.launch_load()


    def launch_load(self):
        thread = threading.Thread(target=self.load_json, args=())
        thread.start()


    def load_json(self):

        response = requests.get('https://raw.githubusercontent.com/llorchcluni/Desing-de-Interfaces/master/JuegoAhorcado/API-REST/catalog.json')

        json_list = response.json()

        result = []


        for json_item in json_list:
            fallos = json_item.get('fallos')

            url_imagen = json_item.get('url_imagen')

            r = requests.get(url_imagen, stream=True)
            with open('temp.png','wb') as f:
                shutil.copyfileobj(r.raw, f)
            image = Gtk.Image.new_from_file('temp.png')
            result.append({"fallos": fallos, "gtk image": image})



        GLib.idle_add(self.start_main_window, result)


    def start_main_window(self, listaObj):
        win = MainWindow(listaObj)
        
        win.show_all()

        self.disconnect_by_func(Gtk.main_quit)

        self.close()


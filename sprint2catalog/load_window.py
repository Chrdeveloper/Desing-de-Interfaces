import shutil

import gi
import requests, threading
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GLib
from window import MainWindow

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

    def launch_load(self):
        thread = threading.Thread(target=self.load_json, args=())
        thread.start()


    def load_json(self):
        response = requests.get('https://github.com/llorchcluni/Desing-de-Interfaces/blob/master/API-REST/catalog.json')

        json_list = response.json()

        result = []

        for json_item in json_list:
            name = json_item.get('name')
            description = json_item.get('description')
            image_url = json_item.get('image_url')

            r = requests.get(image_url, stream=True)
            with open('temp.png', 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            image = Gtk.Image.new_from_file('temp.png')
            result.append({"name": name,"description": description, "gtk image": image})

        Glib.idle_add(self.start_main_window, result)


    def start_main_window(self, loaded_items_list):
        win = MainWindow(loaded_items_list)
        win.show_all()
        win.disconnect_by_func(Gtk.main_quit)
        self.close()

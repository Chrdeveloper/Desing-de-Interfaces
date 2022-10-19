import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk#Importamos Gtk del repositorio gi

from window import MainWindow#Importamos el metodo de MainWindow

from load_window import LoadWindow#Importamos el metodo LoadWindow


win = LoadWindow()#Decimos que la ventana es el MainWindow
win.show_all()#Mostramos la ventana asignada previamente

Gtk.main()

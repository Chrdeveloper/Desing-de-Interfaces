import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell
from gi.repository import GdkPixbuf
class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()
    def __init__(self):
        super().__init__(title="Elige mano")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="opciones")
        header.set_subtitle("Piedra gana a tijeras, tijeras gana a papel, papel gana a piedra.")
        header.props.show_close_button = True
        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("images/tijeras.jpg", 500, 500, False)
        image.set_from_pixbuf(pixbuf)
        cell_one = Cell("tijeras", image)

        image2 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("images/piedra.jpg", 500, 500, False)
        image2.set_from_pixbuf(pixbuf)
        cell_two = Cell("piedra", image2)

        image3 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("images/papel.jpg", 500, 500, False)
        image3.set_from_pixbuf(pixbuf)
        cell_three = Cell("papel", image3)

        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
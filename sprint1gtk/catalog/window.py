import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from cell import Cell


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__(title="Catalogo")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="Skins")
        header.set_subtitle("Las mejores skins")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Corki.jpg", 200, 200, False)
        image.set_from_pixbuf(pixbuf)
        cell_one = Cell("Corki actimel", image)

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

        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)

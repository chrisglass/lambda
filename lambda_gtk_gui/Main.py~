import gtk
import gtk.glade
import sys
import os


class Glade_Loader():
	"""Loads up the GLADE interface from the corresponding description XML"""

	def __init__(self):
		self.handlers = {
			"on_menu_item_quit_activate": gtk.main_quit , 
			"on_button1_clicked": self.print_test ,
			"on_Main_window_destroy" : gtk.main_quit
			}
		self.create_glade_ui()

	def print_test(self,widget):
		print widget.name, "was clicked!"

	def create_glade_ui(self):
		self.widgetTree = gtk.glade.XML('glade/lamda_gtk_ui.glade')
		self.widgetTree.signal_autoconnect(self.handlers)
		#print self.widgetTree




if __name__ == "__main__":
	loader = Glade_Loader()
	gtk.main()

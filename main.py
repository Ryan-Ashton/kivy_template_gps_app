from kivymd.app import MDApp
from _mapview import _MapView
import sqlite3
from searchpopupmenu import SearchPopupMenu
from gpshelper import GpsHelper

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.primary_palette = 'BlueGray'
        # Initialize GPS
        GpsHelper().run()

        # Connect to database
        self.connection = sqlite3.connect("data\hospitals.db")
        self.cursor = self.connection.cursor()

        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

MainApp().run()


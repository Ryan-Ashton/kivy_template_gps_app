from kivy.garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu


class Marker(MapMarkerPopup):
    source = "marker.PNG"
    data = []

    def on_release(self):
        # Open up the LocationPopupMenu
        menu = LocationPopupMenu(self.data)
        menu.size_hint = [.8, .9]
        menu.open()
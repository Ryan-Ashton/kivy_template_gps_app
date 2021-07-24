from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu


class Marker(MapMarkerPopup):
    source = "mapview-develop\kivy_garden\mapview\icons\marker.png"
    data = []

    def on_release(self):
        # Open up the LocationPopupMenu
        menu = LocationPopupMenu(self.data)
        menu.size_hint = [.8, .9]
        menu.open()
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marker import Marker

class _MapView(MapView):
    getting_timer = None
    names = []

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_timer.cancel()
        except:
            pass

        self.getting_timer = Clock.schedule_once(self.get_in_fov, 1)

    def get_in_fov(self, *args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM hospital WHERE Latitude > %s AND Latitude < %s AND Longitude > %s AND Longitude < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        hospitals = app.cursor.fetchall()
        for hospital in hospitals:
            name = hospital[1]
            if name in self.names:
                continue
            else:
                self.add(hospital)

    def add(self, hospital):
        # Create the HospitalMarker
        lat, lon = hospital[3], hospital[4]
        marker = Marker(lat=lat, lon=lon)
        marker.data = hospital
        # Add the HospitalMarker to the map
        self.add_widget(marker)

        # Keep track of the marker's name
        name = hospital[1]
        self.names.append(name)
        
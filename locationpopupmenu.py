from typing import Collection
from kivymd.uix.dialog import MDDialog


class LocationPopupMenu(MDDialog):
    def __init__(self, data):
        super().__init__()

        # Set all of the fields of market data
        headers = "Code,Name,Type,Latitude,Longitude,Sector,Open_Closed,State,Local_Hospital_Network_LHN,Primary_Health_Network_area,Min_Beds,Max_Beds,Website,Elective_Surgery_High_Level,Elective_Surgery_Low_Level,Establishment_ID,Medicare_provider_no,Network_code,Hospital_Network,Remoteness_area,Number_of_available_beds,Peer_group_name,Establishments_data,Morbidity_data,Emergency_department_data,Elective_Surgery_Waiting_times_data,Non_admitted_patient_aggregate_data,IHPA_funding_designation,Phone_number,Street_address,Suburb,Postcode"
        print(headers)
        headers = headers.split(',')

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = data[i]
            setattr(self, attribute_name, attribute_value)

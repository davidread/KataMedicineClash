from datetime import date, timedelta

class Medicine(object):
    
    def __init__(self, name):
        self.name = name
        self.prescriptions = []
        
    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)

    def dates_taken_in_past_x_days(self, day_count):
        return set.union(*[prescription.dates_taken_in_past_x_days(day_count)
                           for prescription in self.prescriptions])


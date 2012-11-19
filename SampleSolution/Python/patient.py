
class Patient(object):
    
    def __init__(self, medicines = None):
        self._medicines = medicines or []
    
    def add_medicine(self, medicine):
        self._medicines.append(medicine)
    
    def clash(self, medicines, days):
        if not medicines:
            return set()
        return set.intersection(*[set(medicine.dates_taken_in_past_x_days(days))
                                  for medicine in medicines])

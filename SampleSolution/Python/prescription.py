from datetime import timedelta, date

class Prescription(object):
    
    def __init__(self, dispense_date=None, days_supply=30):
        self.dispense_date = dispense_date or date.today()
        self.days_supply = days_supply
    
    def dates_taken(self):
        return [self.dispense_date + timedelta(days=i) for i in range(self.days_supply)]

    def dates_taken_in_past_x_days(self, day_count):
        return set(filter(lambda date_taken: (date.today() - timedelta(day_count)) <= date_taken < date.today(),
                          self.dates_taken()))

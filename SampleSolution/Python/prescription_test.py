import unittest
from datetime import date, timedelta
from prescription import Prescription

class PrescriptionTest(unittest.TestCase):
    
    def test_dates_taken_in_past_x_days(self):
        prescription = Prescription( \
            dispense_date=(date.today() - timedelta(days=2)),
            days_supply=4)
        self.assertEquals(set([date.today() - timedelta(days=2),
                               date.today() - timedelta(days=1)]),
                          prescription.dates_taken_in_past_x_days(2))
        
    def test_dates_taken_when_dates_overlap(self):
        prescriptions = [Prescription(dispense_date=date(2009, 12, 1),
                                      days_supply = 2),
                         Prescription(dispense_date=date(2009, 12, 2),
                                      days_supply = 2))
        self.assertEquals([date(2009, 12, 1),
                           date(2009, 12, 2),
                           date(2009, 12, 3)],
                          self.medicine.dates_taken_in_past_x_days(5))

if __name__ == "__main__":
    unittest.main()

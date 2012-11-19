import unittest

from datetime import date, timedelta

from prescription import Prescription
from medicine import *

class MedicineTest(unittest.TestCase):
    
    def setUp(self):
        self.medicine = Medicine("Aspirin")

    def test_dates_taken_in_past_x_days(self):
        self.medicine.add_prescription(
            Prescription(dispense_date=date.today() - timedelta(days=2),
                         days_supply=2))
        self.assertEquals(set([date.today() - timedelta(days=2),
                               date.today() - timedelta(days=1)]),
                          self.medicine.dates_taken_in_past_x_days(2))

    def test_dates_taken_in_past_x_days_when_dates_overlap(self):
        self.medicine.add_prescription(
            Prescription(dispense_date=date.today() - timedelta(days=4),
                         days_supply=2))
        self.medicine.add_prescription(
            Prescription(dispense_date=date.today() - timedelta(days=3),
                         days_supply=2))
        self.assertEquals(set([date.today() - timedelta(days=4),
                               date.today() - timedelta(days=3),
                               date.today() - timedelta(days=2)]),
                          self.medicine.dates_taken_in_past_x_days(5))
    
    def test_dates_taken_in_past_x_days_when_dates_are_in_future(self):
        self.medicine.add_prescription(
            Prescription(dispense_date=(date.today() - timedelta(days=2)),
                         days_supply=4))
        self.assertEquals(set([date.today() - timedelta(days=2),
                               date.today() - timedelta(days=1)]),
                          self.medicine.dates_taken_in_past_x_days(3))
        
if __name__ == "__main__":
    unittest.main()

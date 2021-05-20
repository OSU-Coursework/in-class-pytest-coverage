# cs362 - in class activity 04
# casey nord
# spring 2021


import unittest


class LeapYearUnitTests(unittest.TestCase):

    def test_valid_leapyears(self):
        self.assertEqual(leap_year(1904), True)
        self.assertEqual(leap_year(1984), True)
        self.assertEqual(leap_year(1732), True)
        self.assertEqual(leap_year(2016), True)
    
    def test_invalid_leapyears(self):
        self.assertEqual(leap_year(2021), False)
        self.assertEqual(leap_year(1818), False)
        self.assertEqual(leap_year(1945), False)
        self.assertEqual(leap_year(1623), False)


if __name__ == '__main__':
    unittest.main()

import unittest
from Function import facebookLogin, resetDatabase, scrap


class Test_scrapping(unittest.TestCase):
    # Testing scrap function for the first time\
    def test_scrappingFirst(self):
        resetDatabase()
        self.assertEqual(scrap("radhikagarg1601"), "Scrapped")
        self.assertEqual(scrap("anshul.d.sharma.7"), "Scrapped")
        self.assertEqual(scrap("utkarsh.parkhi.1"), "Scrapped")
        self.assertEqual(scrap("rishi.ranjan.54966"), "Scrapped")
        self.assertEqual(scrap("ritvik.jain.52206"), "Scrapped")

    # Testing scrap function for the second time
    def test_scrappingSecond(self):
        self.assertEqual(scrap("radhikagarg1601"), "Show function")
        self.assertEqual(scrap("anshul.d.sharma.7"), "Show function")
        self.assertEqual(scrap("utkarsh.parkhi.1"), "Show function")
        self.assertEqual(scrap("rishi.ranjan.54966"), "Show function")
        self.assertEqual(scrap("ritvik.jain.52206"), "Show function")

    # Testing the decorator function
    def test_decorator(self):
        with self.assertRaises(Exception):
            scrap("radhikaarg1601")
        with self.assertRaises(Exception):
            scrap("a.divyansh.25")

    # Testing Facebook Login
    def test_login(self):
        with self.assertRaises(Exception):
            facebookLogin("a.divyansh.25@gmail.com", "123456789")


if __name__ == '__main__':
    unittest.main()

import unittest
import constant
from Function import facebookLogin, resetDatabase, scrap, driver


class Test_scrapping(unittest.TestCase):
    def test_scrappingFirst(self):
        resetDatabase()
        self.assertEqual(scrap(constant.radhika), "Scrapped")
        self.assertEqual(scrap(constant.anshul), "Scrapped")
        self.assertEqual(scrap(constant.utkarsh), "Scrapped")
        self.assertEqual(scrap(constant.rishi), "Scrapped")
        self.assertEqual(scrap(constant.ritvik), "Scrapped")

    def test_scrappingSecond(self):
        self.assertEqual(scrap(constant.radhika), "Show function")
        self.assertEqual(scrap(constant.anshul), "Show function")
        self.assertEqual(scrap(constant.utkarsh), "Show function")
        self.assertEqual(scrap(constant.rishi), "Show function")
        self.assertEqual(scrap(constant.ritvik), "Show function")

        driver.close()

    def test_decorator(self):
        with self.assertRaises(Exception):
            scrap("radhikaarg1601")
        with self.assertRaises(Exception):
            scrap("a.divyansh.25")

    def test_login(self):
        with self.assertRaises(Exception):
            facebookLogin("a.divyansh.25@gmail.com", "123456789")


if __name__ == '__main__':
    unittest.main()

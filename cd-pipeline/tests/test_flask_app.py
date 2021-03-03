#!/usr/bin/python 

import os
import sys
import unittest
import app

class BasicTest(unittest.TestCase):

    #execute before each test
    def setUp(self):
        self.app = app.app.test_client()

    #execute after each test
    def tearDown(self):
        pass

    #test
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=Tue)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
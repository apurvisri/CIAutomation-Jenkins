#!/usr/bin/python 

import os
import sys
import unittest
# Flask application we wrote
import app

#This uses the unittest framework
#setUp and tearDown are common methods in testing frameworks, used to initialised the mock objs 
#or tasks and clean up the env after a test is executed
class BasicTest(unittest.TestCase):
    
    #execute before each test to mock a flask app
    def setUp(self):
        self.app = app.app.test_client()

    #execute after each test 
    def tearDown(self):
        pass

    #test, this methods gets the mock falsk app and checks that the root of the app returns 200 http status code  
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

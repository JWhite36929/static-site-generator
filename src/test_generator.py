import unittest 
from page_generator import (
    extract_title,

)

class TestPageGenerator(unittest.TestCase):

    def test_extract_title_valid(self):
        md = """# This is the Title"""
        title = extract_title(md)
        self.assertEqual(title, "This is the Title")
    
    def test_extract_title_no_title(self):
        md = """This document has no title"""
        self.assertRaises(ValueError, extract_title, md)
    
    def test_extract_title_empty(self):
        md = """"""
        self.assertRaises(ValueError, extract_title, md)    
    
    
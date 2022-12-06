#!/usr/bin/python3
""" class to test console docs """

import pep8
import console
import inspect
import unittest
HBNBCommand = console.HBNBCommand

class TestConsoleDocs(unittest.TestCase):
    """ testing documentation of the console """
    def test_pep8_conformance_console(self):
        """ test for console.py conforms pep8 """
        pep8_ = pep8.StyleGuide(quiet=True)
        result = pep8_.check_files(['console.py'])
        self.assertEqual(result.totl_errors, 0,
        "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        pep8_ = pep8.StyleGuide(quiet=True)
        result = pep8_.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

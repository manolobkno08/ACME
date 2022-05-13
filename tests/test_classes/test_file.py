"""
Unittest for File class

"""

import unittest
import classes
import pep8

from classes.file import File


class test_file_docs(unittest.TestCase):
    """Testing documentation of the File class"""

    def test_pep8_conformance_file(self):
        """Test that File class conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['classes/file.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file(self):
        """Test that tests/test_file.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_classes/test_file.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_file_methods(unittest.TestCase):
    """Testing file class methods"""

    def test_File(self):
        """Testing singleton file class with unique instance"""
        object1 = File()
        object2 = File()
        # If the check fails
        message = "given objects are not the same instance"
        # assertIsInstance() to check if obj is instance of class
        self.assertIs(object1, object2, message)


if __name__ == '__main__':
    """Main Unittest"""
    unittest.main()

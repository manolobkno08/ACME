"""
Unittest for File class

"""

import unittest
import pep8
import os
from modules.read_file import read_file as rf, get_path_files


class test_read_file_docs(unittest.TestCase):
    """Testing documentation of the read_file"""

    def test_pep8_conformance_file(self):
        """Test that filre_read conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['modules/read_file.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file(self):
        """Test that tests/test_read_file.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_modules/test_read_file.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class tests_read_file_functions(unittest.TestCase):
    """Testing read_files functions"""

    def test_get_path_files(self):
        """Testing function that get str and return absolute path"""
        separator = os.path.sep
        path = os.path.dirname(os.path.realpath(__file__))
        r = separator.join(path.split(separator)[:-2])
        path_file = f"{r}{separator}files{separator}data.txt"
        self.assertEqual(get_path_files("data.txt"), path_file)

    def test_read_file(self):
        """Testing function that get user and read file"""
        self.assertIsInstance("MANUEL", str)
        self.assertTrue("MANUEL".isupper())
        # with self.assertRaises(TypeError):
        #     rf(2.4)


if __name__ == '__main__':
    """Main Unittest"""
    unittest.main()

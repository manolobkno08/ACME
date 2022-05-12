"""
Unittest for File class

"""

import unittest
import pep8

from modules.read_file import read_file


class test_read_file_docs(unittest.TestCase):
    """Testing documentation of the read_file"""

    def test_pep8_conformance_file(self):
        """Test that File class conforms to PEP8."""
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


if __name__ == '__main__':
    """Main Unittest"""
    unittest.main()

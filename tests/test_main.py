"""
Unittest for main

"""

import unittest
import main
import pep8
ACMECommand = main.ACMECommand


class test_main_docs(unittest.TestCase):
    """Testing documentation of the main"""

    def test_pep8_conformance_main(self):
        """Test that main.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['main.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_main(self):
        """Test that tests/test_main.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_main.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_ACMECommand_function_docstring(self):
        """Test for the ACMECommand docstring"""
        self.assertIsNot(ACMECommand.__doc__, None,
                         "ACMECommand needs a docstring")
        self.assertTrue(len(ACMECommand.__doc__) >= 1,
                        "ACMECommand needs a docstring")


if __name__ == '__main__':
    """Main Unittest"""
    unittest.main()

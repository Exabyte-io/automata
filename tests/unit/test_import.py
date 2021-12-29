import unittest

import automata

class TestVersion(unittest.TestCase):

    def test_version(self):
        print("AHH", automata.__version__)
        self.assertIsNotNone(automata.__version__)

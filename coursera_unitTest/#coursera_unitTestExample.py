#coursera_unitTestExample


from lettercom import LetterCompiler
import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['a', 'b']
        self.assertEqual(LetterCompiler(my_txt), expected)
#coursera_unitTestExample


from lettercom import LetterCompiler
import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "An investment in knowledge pays the best interest."
        expected = ['a', 'b']
        self.assertEqual(LetterCompiler(testcase), expected)

        
    def test_empty(self):
        testcase = ""
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

        
    def test_num(self):
        testcase = "101"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

        
    def test_diffStr(self):
        testcase = "We are here to learn"
        expected = ['a', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)
        
unittest.main()
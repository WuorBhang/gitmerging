import unittest

from solutions.char_present_in_word import char_present_in_word

class TestCharPresentInWord(unittest.TestCase):
    """checking present of a str in in the given word: mango"""
    def test_letter_a_present(self):
        actual = char_present_in_word("a", "mango")
        expected = True
        self.assertEqual(actual, expected)
    
    def test_letter_b_present(self):
        """checking the present b in the given word: boy"""
        actual = char_present_in_word("b", "boy")
        expected = True
        self.assertEqual(actual, expected)

    def test_letter_c_present(self):
        """checking the present c in the given word: cat"""
        actual = char_present_in_word("c", "cat")
        expected = True
        self.assertEqual(actual, expected)
      
    def test_letter_d_present(self):
        """checking the present d in the given word: dog"""
        actual = char_present_in_word("d", "Hotel")
        expected = False 
        self.assertEqual(actual, expected)

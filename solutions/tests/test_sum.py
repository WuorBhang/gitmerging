import unittest

from solutions.sum import sum

class TestSum(unittest.TestCase):
  
  """It should return the sum of a positive numbers"""
  def test_sum_positive_numbers(self):
    actual = sum(1, 2, 3, 4, 5)
    expected = 15
    self.assertEqual(actual, expected)
    
  """It should return the sum of a negative numbers"""
  def test_sum_negative_numbers(self):
    actual = sum(-1, -2, -3, -5)
    expected = -11
    self.assertEqual(actual, expected)

  """It should return the sum of a mix numbers"""
  def test_sum_mixed_numbers(self):
    actual = sum(10, -20, -40, 50)
    expected = 0
    self.assertEqual(actual, expected)

  """It should return the sum of a float numbers"""
  def test_sum_float_numbers(self):
    actual = sum(1.5, 2.5, 3.7, 4.5)
    expected = 12.2
    self.assertEqual(actual, expected)

  """It should return the sum of zero numbers"""
  def test_sum_zero_numbers(self):
    actual = sum(0, 0, 0, 0)
    expected = 0
    self.assertEqual(actual, expected)

import random
import unittest

import happyentropy

class ConversionTest(unittest.TestCase):
  def setUp(self):
    super(ConversionTest, self).setUp()
    random.seed(0)

  def testRoundTrip(self):
    for _ in range(100000):
      n = random.randint(0, 2 ** 32 - 1)
      self.assertEqual(
          happyentropy.sentence_to_number(happyentropy.number_to_sentence(n)), n)

  def testNegativeNumber(self):
    with self.assertRaises(AssertionError):
      happyentropy.number_to_sentence(-1)

  def testTooBig(self):
    with self.assertRaises(AssertionError):
      happyentropy.number_to_sentence(2 ** 32)

  def testSentenceTooShort(self):
    with self.assertRaises(ValueError):
      happyentropy.sentence_to_number('asdf asdf')

  def testSentenceTooLong(self):
    with self.assertRaises(ValueError):
      happyentropy.sentence_to_number('asdf asdf asdf asdf asdf asdf asdf asdf')

if __name__ == '__main__':
  unittest.main()

import unittest
from happyentropy import vocab

def all_unique(lst):
  return len(set(lst)) == len(lst)

class VocabTest(unittest.TestCase):
  def testLengths(self):
    self.assertEqual(len(vocab.COUNTS), 32)
    self.assertEqual(len(vocab.ADJECTIVES), 128)
    self.assertEqual(len(vocab.ANIMALS), 128)
    self.assertEqual(len(vocab.VERBS), 128)
    self.assertEqual(len(vocab.ADVERBS), 64)

  def testUnique(self):
    self.assertTrue(all_unique(vocab.COUNTS))
    self.assertTrue(all_unique(vocab.ADJECTIVES))
    self.assertTrue(all_unique(vocab.ANIMALS))
    self.assertTrue(all_unique(vocab.VERBS))
    self.assertTrue(all_unique(vocab.ADVERBS))

if __name__ == '__main__':
  unittest.main()

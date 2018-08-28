import random

from happyentropy.vocab import DEFAULT_VOCAB

def number_to_sentence(n, vocab=DEFAULT_VOCAB):
  assert n >= 0, 'Number must be non-negative!'
  assert n < 2 ** 32, 'Number must be less than 2^32!'
  counts, adjectives, animals, verbs, adverbs = vocab
  count = counts[(n >> 27) & (2 ** 5 - 1)]
  adjective = adjectives[(n >> 20) & (2 ** 7 - 1)]
  animal = animals[(n >> 13) & (2 ** 7 - 1)] + 's'
  verb = verbs[(n >> 6) & (2 ** 7 - 1)]
  adverb = adverbs[n & (2 ** 6 - 1)]
  return ' '.join([count, adjective, animal, verb, adverb])

def sentence_to_number(sentence, vocab=DEFAULT_VOCAB):
  counts, adjectives, animals, verbs, adverbs = vocab
  count, adjective, animal, verb, adverb = sentence.split(' ')
  return (
    (counts.index(count) << 27) +
    (adjectives.index(adjective) << 20) +
    (animals.index(animal[:-1]) << 13) +
    (verbs.index(verb) << 6) +
    adverbs.index(adverb)
  )

def random_sentence(vocab=DEFAULT_VOCAB):
  return number_to_sentence(random.randint(0, 2 ** 32 - 1), vocab=vocab)

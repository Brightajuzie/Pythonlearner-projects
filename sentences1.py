import random  # Import the random module

def get_preposition():
  """Return a random preposition."""
  prepositions = ["in", "on", "at", "by", "with", "from", "into"]
  return random.choice(prepositions)

def get_adverb():
  """ Returns random adverb"""
  adverbs = ["quickly", "slowly", "angrily", "fastly", "softly", "beautifully", "greedily"]
  return random.choice(adverbs)

def get_determiner(quantity):
  """Return a randomly chosen determiner.

  Args:
    quantity: An integer. If quantity is 1, this function will return a
              determiner for a singular noun. Otherwise, this function will return
              a determiner for a plural noun.

  Returns:
    A randomly chosen determiner (string).
  """
  if quantity == 1:
    words = ["a", "one", "the"]
  else:
    words = ["some", "many", "the"]
  return random.choice(words)


def get_noun(quantity):
  """Return a randomly chosen noun.

  Args:
    quantity: An integer that determines if the returned noun is singular or plural.

  Returns:
    A randomly chosen noun (string).
  """
  if quantity == 1:
    nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
  else:
    nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
  return random.choice(nouns)


def get_verb(quantity, tense):
  """Return a randomly chosen verb.

  Args:
    quantity: An integer that determines if the returned verb is singular or plural.
    tense: A string that determines the verb conjugation (past, present, or future).

  Returns:
    A randomly chosen verb (string).
  """
  if tense == "past":
    verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
  elif tense == "present":
    if quantity == 1:
      verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    else:
      verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
  else:
    verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep",
              "will talk", "will walk", "will write"]
  return random.choice(verbs)


def make_sentence(quantity, tense):
  """Build and return a sentence with three words: determiner, noun, and verb,
  followed by a prepositional phrase and an adverbial phrase.

  Args:
    quantity: An integer (singular or plural).
    tense: A string (past, present, or future).

  Returns:
    A grammatically correct sentence (string).
  """
  determiner = get_determiner(quantity)
  noun = get_noun(quantity)
  verb = get_verb(quantity, tense)
  preposition = get_preposition()
  prepositional_article = get_determiner(quantity)  # Use the same quantity for prepositional determiner
  prepositional_noun = get_noun(1)  # Use singular noun for prepositional phrase
  adverb = get_adverb()  # Include adverb

  sentence = f"{determiner} {noun} {verb} {preposition} {prepositional_article} {prepositional_noun} {adverb}."
  return sentence.capitalize()


def main():
  """Calls make_sentence function six times with different quantities and tenses, printing the sentences."""

  quantities = [1, 1, 1, 2, 2, 2]
  tenses = ["past", "present", "future", "past", "present", "future"]

  for i in range(6):
    sentence = make_sentence(quantities[i], tenses[i])
    print(sentence)

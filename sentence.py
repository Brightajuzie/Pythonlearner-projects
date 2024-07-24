import random


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

def get_preposition():
    """Return a randomly chosen preposition
from this list of prepositions:
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"

Return: a randomly chosen preposition.
"""
    preposition =["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    return random.choice(preposition)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
of three words: a preposition, a determiner, and a
noun by calling the get_preposition, get_determiner,
and get_noun functions.

Parameter
    quantity: an integer that determines if the
        determiner and noun in the prepositional
        phrase returned from this function should
        be single or pluaral.
Return: a prepositional phrase.
"""
    

def make_sentence(quantity, tense):
    """Build and return a sentence with three words: determiner, noun, and verb.

    Args:
        quantity: An integer (singular or plural).
        tense: A string (past, present, or future).

    Returns:
        A grammatically correct sentence (string).
    """

    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)

    sentence = f"{determiner} {noun} {verb}."
    return sentence.capitalize()  # Capitalize the first letter


def main():
    """Calls make_sentence function six times with different quantities and tenses, printing the sentences."""

    quantities = [1, 1, 1, 2, 2, 2]
    tenses = ["past", "present", "future", "past", "present", "future"]

    for i in range(6):
        sentence = make_sentence(quantities[i], tenses[i])
        print(sentence)


if __name__ == "__main__":
    main()

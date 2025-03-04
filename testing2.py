"""
Author: Brother Burton
Purpose: Capitalizes letters in a string.
"""

word = "commitment"

favorite_letter = input("What is your guess? ")

###
# Core Requirements #1 and #2
###
for [i] in word:
    # Just in case the word or the user's letter contain a capital, we
    # should convert the letters to lowercase when we compare them
    if [i].lower() == favorite_letter.lower():
        print([i].upper(), end="")
    else:
        print([i].lower(), end="")
print()

###
# Core Requirement #3
###
for letter in word:
    # Just in case the word or the user's letter contain a capital, we
    # should convert the letters to lowercase when we compare them
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()
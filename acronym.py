"""
Get acronym from phrase
"""

while True:
    words = input()

    acronym = ''.join(word[0].upper() for word in words.split())

    print(acronym + "\n")

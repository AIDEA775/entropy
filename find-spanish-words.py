#!/usr/bin/python
"""Find Words.

Usage:
  findSpanishWords.py <dic> <letters> <len>
  findSpanishWords.py (-h | --help)

Options:
  -h --help     Show this screen.

"""

from docopt import docopt

def checkWord(realWord, letters):
    rest = letters
    for l in realWord:
        if l not in rest:
            return False
        else:
            rest = rest.replace(l, '', 1)
    return True

def find(dic, letters, size):
    for w in dic:
        if len(w) == size and checkWord(w, letters):
            print(w)

if __name__ == '__main__':
    args = docopt(__doc__, version='0')

    with open(args['<dic>']) as f:
        dic = f.readlines()

    dic = [x.strip() for x in dic]
    
    find(dic, args['<letters>'], int(args['<len>']))


#!/usr/bin/python
"""Find the possible words with the specific letters and length.

Usage:
  %name% <dictionary> <letters> <length>
  %name% (-h | --help)

Options:
  -h --help     Show this screen.

"""
import sys
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
    progName=sys.argv[0]
    args = docopt(__doc__.replace('%name%',progName), help=True)

    with open(args['<dictionary>']) as f:
        dic = f.readlines()

    dic = [x.strip() for x in dic]
    
    find(dic, args['<letters>'], int(args['<length>']))


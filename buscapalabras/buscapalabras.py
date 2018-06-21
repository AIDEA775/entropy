#!/usr/bin/python
"""Find the possible words with the specific letters and length.

Usage:
  %name% [-d FILE] <letters> <length>
  %name% (-h | --help)

Options:
  -d FILE --dictionary=FILE  Dictionary to use [default: %path%/default.txt]
  -h --help                  Show this screen.

"""
import sys, os
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
    name = os.path.basename(sys.argv[0])
    path = os.path.dirname(os.path.abspath(__file__))
    args = docopt(__doc__.replace('%name%', name).replace('%path%', path))

    with open(args['--dictionary']) as f:
        dic = f.readlines()

    dic = [x.strip() for x in dic]
    
    find(dic, args['<letters>'], int(args['<length>']))


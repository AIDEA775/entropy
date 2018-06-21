import re
import os

def words(text): return re.findall(r'\w+', text.lower())

word_list = os.path.join(os.path.dirname(__file__), "lemario.txt")
WORDS = words(open(word_list).read())

def P(pair):
    return pair[1]

def correction(word):
    "La mejor corrección"
    if word in WORDS:
        return word
    return correct(word)[0]

def correct(word):
    "La mejor probable corrección con su peso"
    return min(candidates(word), key=P)

def candidates(word):
    editsAll = set(editsOne(word) + editsTwo(word))
    return [(w, v) for w, v in editsAll if known(w)] + [(word, 99)]

def known(word):
    return word in WORDS

def edit1(word):
    "Falta de H"
    return [word[:i] + 'h' + word[i:] for i in range(len(word)+1)]

def edit2(word):
    "Falta de acentos"
    vocals = 'aeiou'
    accents = 'áéíóú'
    return [word[:i] + accents[vocals.find(word[i])] + word[i+1:] for i in range(len(word)) if word[i] in vocals]

def edit3(word):
    "Sonidos parecidos"
    cons = ['bv', 'csz', 'iy', 'ckq']
    return [word[:i] + k + word[i+1:] for j in cons for i in range(len(word)) if word[i] in j for k in j]

def edit4(word):
    "Doble consonante"
    cons = [('r', 'rr'), ('y', 'll'), ('k', 'qu')]
    return [word.replace(i, k, 1) for c in cons for i in c if i in word for k in c]

def editsOne(word):
    "Candidatas con un cambio"
    load = {edit1 : 1, edit2 : 2, edit3 : 3, edit4 : 4}
    return [(j, load.get(i)) for i in load.keys() for j in i(word)]

def editsTwo(word):
    "Candidatas con dos cambios"
    return [(ee, v + vv)  for e, v in editsOne(word) for ee, vv in editsOne(e)]



"""
def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N

def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'aábcdeéfghiíjklmnñoópqrstuúvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
"""

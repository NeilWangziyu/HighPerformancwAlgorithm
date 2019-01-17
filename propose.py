t9 = "22233344455566677778889999"
def letter_digit(x):
    for each in x:
        return t9[ord(x)-ord('a')]


def word_code(words):
    return "".join(map(letter_digit, words))

def predictive_text(dico):
    freq = {}
    for words, weights in dico:
        prefix = ""
        for x in words:
            prefix += x
            if prefix in freq:
                freq[prefix] += weights
            else:
                freq[prefix] = weights
    prop = {}
    for prefix in freq:
        code = word_code(prefix)
        if code not in prop or freq[prop[code]] < freq[prefix]:
            prop[code] = prefix
    return prop

def propose(prop, seq):
    if seq in prop:
        return prop[seq]
    else:
        return "None"



print(word_code('bonjour'))
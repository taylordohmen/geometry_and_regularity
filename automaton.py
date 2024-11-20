from itertools import product
from functools import reduce
from math import log2

# word: tuple<(symbol,symbol)>
# base: positive integer
def value(word, base):
    x_val, y_val = 0, 0
    for index, symbol_pair in enumerate(word):
        x_coord, y_coord = symbol_pair
        x_val += x_coord * base**(-(index + 1))
        y_val += y_coord * base**(-(index + 1))
    return (x_val, y_val)

# language: set< tuple<(symbol,symbol)> >
# base: positive integer
def interpret(language, base):
    return {value(w, base) for w in language}


class Automaton:

    # alphabet: set{symbol}
    # states: set{state_type}
    # initial: state_type
    # final: set{state_type}
    # delta: dict{ (state_type, symbol) ->  set{state_type} }
    # state_type: enum
    def __init__(self, alphabet, initial, final, delta, state_type):
        self.alphabet = alphabet
        self.states = reduce(lambda x, y: x | y, state_type)
        self.initial = initial
        self.final = final
        self.delta = delta
        self.state_type = state_type

    # state: state_type
    # word: list<symbol>
    def delta_star(self, state, word):
        if len(word) == 0:
            return state
        head, tail = word[0], word[1:]
        if (state, head) in self.delta:
            return reduce(
                lambda x, y: x | y,
                {self.delta_star(q, tail) for q in self.delta[(state, head)]}
            )
        else:
            return self.state_type(0)
    
    # word: list<symbol>
    def accepts(self, word):
        ret = self.delta_star(self.initial, word)
        if bool(ret & self.final):
            return True
        else:
            return False
    
    # max_length: non-negative integer
    def language(self, max_length):
        lang = set()
        for n in range(max_length + 1):
            words = product(self.alphabet, repeat = n)
            words = {w + ((0,0),)*int(log2(len(self.alphabet))) for w in words}
            lang |= {w for w in words if self.accepts(w)}
        return lang        
        
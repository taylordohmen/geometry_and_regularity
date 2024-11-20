from itertools import product
from util import *

# word: tuple<symbol>
# base: positive integer
def num_value(word, base):
    return sum(digit * base**(-(i + 1)) for i, digit in enumerate(word))

# language: set{ (tuple<symbol>, tuple<symbol>) }
# base: positive integer
def interpret(relation, base):
    return {(num_value(x, base), num_value(y, base)) for x, y in relation}

class SST:

    # alphabet: set{symbol}
    # initial: state_type
    # final_output: dict{ state_type -> tuple< tuple<symbol> | var_type > }
    # delta: dict{ (state_type, symbol) ->  tuple<(state_type, assign_type)> }
    # state_type: enum
    # var_type: enum
    def __init__(self, alphabet, state_type, var_type, initial_state, final_output, delta):
        self.alphabet = alphabet
        self.state_type = state_type
        self.var_type = var_type
        self.initial_state = initial_state
        self.final_output = final_output
        self.delta = delta

    # expression: tuple< symbol | var_type >
    # var_vals: tuple< tuple<symbol> >
    def evaluate(self, expression, var_vals):
        value = tuple()
        for term in expression:
            if isinstance(term, self.var_type):
                value += var_vals[term-1]
            else:
                value += (term,)
        return value

    # var_vals: tuple< tuple<symbol> >
    # update: dict{ var_type -> tuple< symbol | var_type > }
    def reassign(self, var_vals, update):
        new_var_vals = tuple()
        for variable in update:
            new_var_vals += (self.evaluate(update[variable], var_vals),)
        return new_var_vals

    # configs: set{ ( state_type, tuple< tuple<symbol> > ) }
    # word: tuple<symbol>
    def delta_star(self, configs, word):
        if not configs:
            return None
        if not word:
            return configs
        head, tail = word[0], word[1:]
        successor_configs = set()
        for state, var_state in configs:
            if (state, head) in self.delta:
                for next_state, assignment in self.delta[(state, head)]:
                    next_var_state = self.reassign(var_state, assignment)
                    successor_configs |= {(next_state, next_var_state)}
        return self.delta_star(successor_configs, tail)
    
    # word: tuple<symbol>
    def process(self, word):
        init = {(self.initial_state, tuple(tuple() for i in range(len(self.var_type))))}
        # print(init)
        # print(word)
        end_configs = self.delta_star(init, word)
        # print(end_configs)
        image = set()
        if end_configs:
            for state, var_state in end_configs:
                if state in self.final_output:
                    image |= {self.evaluate(self.final_output[state], var_state)}
        return image

    # max_input_length: non-negative integer
    def relation(self, max_input_length):
        input_words = set()
        for n in range(max_input_length + 1):
            input_words |= {w + (0,) for w in product(self.alphabet, repeat = n)}
        pair_set = set()
        for in_word in input_words:
            pair_set |= {(in_word, out_word) for out_word in self.process(in_word)}
        return pair_set
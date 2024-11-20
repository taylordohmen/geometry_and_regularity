from enum import Flag, auto
from itertools import product
import matplotlib.pyplot as plt
from math import pi
from automaton import *

class State(Flag):
    A = auto()
    B = auto()
    C = auto()

dimension = 2
base = 2

alphabet = set(product(range(base), repeat = dimension))
initial = State.A
final = State.B
delta = {
    (State.A, (0, 0)): State.B,
    (State.A, (0, 1)): State.C,
    (State.A, (1, 1)): State.C,
    (State.A, (1, 0)): State.C,
    (State.B, (0, 0)): State.B,
    (State.B, (0, 1)): State.B,
    (State.B, (1, 1)): State.B,
    (State.B, (1, 0)): State.B,
    (State.C, (0, 0)): State.C,
    (State.C, (0, 1)): State.C,
    (State.C, (1, 1)): State.C,
    (State.C, (1, 0)): State.C
}

square = Automaton(alphabet, initial, final, delta, State)

max_length = 9
language = square.language(max_length)
interpretation = interpret(language, base)

x, y = zip(*interpretation)

# fig = plt.figure()
# cartesian = plt.subplot(121)
# polar = plt.subplot(122, projection='polar')
# cartesian.scatter(x, y, marker = '.')
# polar.scatter(list(map(lambda z : z * pi *2, y)), x, marker = '.')
# plt.show()

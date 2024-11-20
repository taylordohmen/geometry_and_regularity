from enum import Flag, auto
from itertools import product
import matplotlib.pyplot as plt
from math import pi
from automaton import *

class State(Flag):
    A = auto()
    B = auto()
    C = auto()
    D = auto()

dimension = 2
base = 2

alphabet = set(product(range(base), repeat = dimension))
initial = State.A
final = State.C | State.D
delta = {
    (State.A, (1, 1)): State.B,

    (State.B, (1, 1)): State.C,

    (State.C, (0, 1)): State.C,
    (State.C, (1, 0)): State.C,
    (State.C, (1, 1)): State.D,

    (State.D, (0, 0)): State.D,
    (State.D, (0, 1)): State.D,
    (State.D, (1, 0)): State.D,
    (State.D, (1, 1)): State.D
}

triangle = Automaton(alphabet, initial, final, delta, State)

max_length = 7
language = triangle.language(max_length)
interpretation = interpret(language, base)

x, y = zip(*interpretation)

fig = plt.figure()
cartesian = plt.subplot(121)
cartesian.set_xlim(left=0, right=1)
cartesian.set_ylim(bottom=0, top=1)
polar = plt.subplot(122, projection='polar')
cartesian.scatter(x, y)
polar.scatter(list(map(lambda z : z * pi *2, y)), x)
plt.show()


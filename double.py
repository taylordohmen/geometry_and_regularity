from enum import Enum, IntEnum, auto
from string import ascii_letters
from itertools import product
from math import pi
import matplotlib.pyplot as plt
from sst import *

dimension = 1
base = 2

num_states = 1
num_vars = 2
num_assignments = 2

if dimension == 1:
    alphabet = range(base)
else:
    alphabet = set(product(range(base), repeat = dimension))
State = Enum(
    'State', 
    {char : auto() for char in ascii_letters[:num_states]}
)
Var = IntEnum(
    'Var',
    {char : auto() for char in ascii_letters[:num_vars]}
)
initial_state = State.a
final_output = {
    State.a : (Var.a, Var.b)
}
Update = type(
    'Update',
    (),
    dict(
        a = {
            Var.a : (Var.a, 0),
            Var.b : (Var.b, 0)
        },
        b = {
            Var.a : (Var.a, 1),
            Var.b : (Var.b, 1)
        }
    )
)
delta = {
    (State.a, 0) : ((State.a, Update.a),),
    (State.a, 1) : ((State.a, Update.b),)
}

T_double = SST(alphabet, State, Var, initial_state, final_output, delta)


for n in range(20):
    w = tuple(int(d) for d in bin(n)[2:])
    print(w, '------T----->' ,T_double.process(w))


# x, y = zip(*interpretation)

# fig = plt.figure()
# cartesian = plt.subplot(121)
# cartesian.set_xlim(left=0, right=1)
# cartesian.set_ylim(bottom=0, top=1)
# polar = plt.subplot(122, projection='polar')
# cartesian.scatter(x, y)
# polar.scatter(list(map(lambda z : z * pi *2, y)), x)
# plt.show()


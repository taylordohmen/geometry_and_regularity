from enum import Enum, IntEnum, auto
from string import ascii_letters
from itertools import product
from math import pi
import matplotlib.pyplot as plt
from sst import *

dimension = 1
base = 2

num_states = 3
num_vars = 2
num_assignments = 4

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
    State.b : (Var.a,),
    State.c : (Var.a,)
}
Update = type(
    'Update',
    (),
    dict(
        a = {
            Var.a : (Var.a,),
            Var.b : (0,)
        },
        b = {
            Var.a : (Var.a, 1),
            Var.b : (Var.b, 0)
        },
        c = {
            Var.a : (Var.a, Var.b, 1),
            Var.b : tuple()
        },
        d = {
            Var.a : (Var.a, 0),
            Var.b : (Var.b,)
        }
    )
)
delta = {
    (State.a, 1) : ((State.b, Update.a),),
    (State.b, 1) : ((State.b, Update.b),),
    (State.b, 0) : ((State.c, Update.c),),
    (State.c, 0) : ((State.c, Update.d),)
}

T_sqr = SST(alphabet, State, Var, initial_state, final_output, delta)


interpretation = interpret(T_sqr.relation(15), base)
x, y = zip(*interpretation)

# fig = plt.figure()
# cartesian = plt.subplot(121)
# cartesian.set_xlim(left=0, right=1)
# cartesian.set_ylim(bottom=0, top=1)
# polar = plt.subplot(122, projection='polar')
# cartesian.scatter(x, y, marker='.')
# polar.scatter(list(map(lambda z : z * pi *2, y)), x, marker = '.')
# plt.show()

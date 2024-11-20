from fractions import Fraction

def binary(frac):
    d = Fraction(1, 2)
    b = []
    while frac > 0:
        if d > frac:
            b += [0]
        else:
            b += [1]
            frac -= d
        d *= Fraction(1, 2)
    return b


for k in range(1, 6):
    denom = 2**k
    for num in range(1, denom // 2 + 1):
        frac = Fraction(num, denom)
        if num == 1 or denom % num != 0:
            b = binary(frac)
            c = binary(1 - frac)
            print(F'{num} / {denom} \t {b} \t 1 - {num} / {denom} \t {c}')
            print(c == [1 - z if i != len(b)-1 else z for i, z in enumerate(b) ])

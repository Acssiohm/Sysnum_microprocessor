################################################################################
######################      LOGIC UNIT         #################################
################################################################################

from lib_carotte import *
from typing import *

def concat(l):
    s = l[0]
    for x in l[1:] :
        s = s + x
    return s

def clone(n, x):
    return concat(n*[x])

def n_binop(f_op, a, b) :
    assert a.bus_size == b.bus_size
    n = a.bus_size
    res_bits = [f_op(a[i], b[i]) for i in range(n)]
    s = concat(res_bits)
    return s

def n_or(a,b):
    return n_binop(lambda x,y : x | y, a, b)

def n_and(a,b):
    return n_binop(lambda x,y : x & y, a, b)

def n_xor(a,b):
    return n_binop(lambda x,y : x ^ y, a, b)

def n_not(a):
    return concat([~a[i] for i in range(a.bus_size)])

def multi_binop(f_op, a):
    assert a.bus_size >= 2
    if a.bus_size == 2 :
        return f_op(a[0], a[1])
    return f_op(a[0], multi_binop(a[1:]) )

def b_and(a):
    return multi_binop(lambda x,y : x & y, a)

def b_or(a):
    return multi_binop(lambda x,y : x | y, a)

def simple_left_shift(a):
    n = a.bus_size
    return Constant("0")+a[:n-1]

def main() -> None :
    n = 4
    a = Input(n)
    b = Input(n)
    n_or(a,b).set_as_output("r_or")
    n_and(a,b).set_as_output("r_and")
    n_xor(a,b).set_as_output("r_xor")
    n_not(a).set_as_output("r_not")
    simple_left_shift(a).set_as_output("r_shift")

# Example:
# a ? 0b1100
# b ? 0b1010
# => r_or = 14 (0b1110)
# => r_and = 8 (0b1000)
# => r_xor = 6 (0b0110)
# => r_not = 3 (0b0011)
# => r_shift = 8 (0b1000)
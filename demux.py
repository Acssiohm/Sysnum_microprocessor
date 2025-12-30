################################################################################
######################      DEMULTIPLEXER         ##############################
################################################################################

from lib_carotte import *
from typing import *

from log_unit import n_and, clone, n_or, concat
from mux import mux

def bit_demux(sel, a) :
    assert sel.bus_size == 1
    assert a.bus_size % 2 == 0
    mid = a.bus_size//2 
    branch0 = n_and(clone(mid, ~sel), a[:mid])
    branch1 = n_and(clone(mid, sel),  a[mid:])
    return n_or(branch0, branch1)

def demux(sel, a):
    if sel.bus_size == 1 :
        return bit_demux(sel, a)
    return demux(sel[1:], bit_demux(sel[0], a))


def main():
    sel = Input(2)
    a = Input(8)

    demux(sel, a).set_as_output("r") 
    demux(sel, concat(mux(sel, a))).set_as_output("id") # devrait donner la même chose que "a"
    concat(mux(sel, demux(sel, a))).set_as_output("p")  # devrait juste mettre les bits non sélectionnées à 0 

# Exemple :
# Step 1 :
# sel ? 3
# a ? 0b11100100
# => r = 3 (0b11)
# => id = 228 (0b11100100)
# => p = 192 (0b11000000)

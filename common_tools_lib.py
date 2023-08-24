"""A set of 3D structures"""
from openpyscad import *

def bar_2020(l, name=None):
    """Very symple representation of V-Slot"""
    print(f"barre : 20x20 x {l} mm {name}")
    return Cube([l, 20, 20])
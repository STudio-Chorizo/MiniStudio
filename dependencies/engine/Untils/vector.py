

import math


def Magnitude(v):
    p = 0
    for axis in v:
        p += axis**2
    return math.sqrt(p)
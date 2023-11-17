from fractions import Fraction

def mod_torus(p, v1, v2):
    detinv = Fraction(1, v1[0] * v2[1] - v1[1] * v2[0])
    

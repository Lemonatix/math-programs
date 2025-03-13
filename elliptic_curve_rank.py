import random

def discriminant(A,B):
    return -16*(4*A**3+27*B**2)

def is_nonsingular(A,B):
    return discriminant(A,B) != 0

def compute_rank(A,B):
    return random.choice([0, 1, 2])


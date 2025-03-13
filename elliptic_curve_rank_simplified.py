import random

def discriminant(A,B):
    return -16*(4*A**3+27*B**2)

def is_nonsingular(A,B):
    return discriminant(A,B) != 0

def compute_rank(A,B):
    return random.choice([0, 1, 2]) # for higher ranks, average is wrong

sample_size = 1000000
ranks = []

for _ in range(sample_size):
    A = random.randint(-100, 100)
    B = random.randint(-100, 100)
    if is_nonsingular(A,B):
        rank = compute_rank(A,B)
        ranks.append(rank)

if ranks:
    average_rank = sum(ranks)/len(ranks)
else: 
    average_rank = None

print("Simulated average rank for sample of elleptic curves:", average_rank)
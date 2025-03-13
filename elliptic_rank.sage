# Define a function to compute the average rank over a range of A and B values
def compute_average_rank(A_min, A_max, B_min, B_max):
    ranks = []
    curves_count = 0
    for A in range(A_min, A_max + 1):
        for B in range(B_min, B_max + 1):
            # In short Weierstrass form: y^2 = x^3 + A*x + B,
            # the Sage constructor is given as [a1, a2, a3, a4, a6]
            # For our case, we take a1=a2=a3=0, a4=A, a6=B.
            E = EllipticCurve([0, 0, 0, A, B])
            # Check nonsingularity: the discriminant should be nonzero.
            if E.discriminant() != 0:
                r = E.rank()  # Compute the rank of the curve
                ranks.append(r)
                curves_count += 1
                print("E: y^2 = x^3 + {}x + {}  has rank: {}".format(A, B, r))
    # Compute the arithmetic mean of the ranks
    average_rank = sum(ranks) / curves_count if curves_count > 0 else None
    return average_rank, curves_count

# Define the range for A and B (small ranges for demonstration purposes)
A_min, A_max = -5, 5
B_min, B_max = -10, 10

# Compute the average rank over the specified family of curves
avg_rank, num_curves = compute_average_rank(A_min, A_max, B_min, B_max)
print("\nComputed average rank over {} curves: {}".format(num_curves, avg_rank))
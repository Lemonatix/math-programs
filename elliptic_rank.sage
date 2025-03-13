def compute_average_rank(A_min, A_max, B_min, B_max):
    ranks = []
    curves_count = 0
    for A in range(A_min, A_max + 1):
        for B in range(B_min, B_max + 1):
            E = EllipticCurve([0, 0, 0, A, B])
            if E.discriminant() != 0:
                r = E.rank()  # Compute the rank of the curve
                ranks.append(r)
                curves_count += 1
                print("E: y^2 = x^3 + {}x + {}  has rank: {}".format(A, B, r))
    average_rank = sum(ranks) / curves_count if curves_count > 0 else None
    return average_rank, curves_count

A_min, A_max = -5, 5
B_min, B_max = -10, 10

avg_rank, num_curves = compute_average_rank(A_min, A_max, B_min, B_max)
print("\nComputed average rank over {} curves: {}".format(num_curves, avg_rank))
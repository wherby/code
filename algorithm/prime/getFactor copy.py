MX = 1_000_001
prime_factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not prime_factors[i]:
        for j in range(i, MX, i):
            prime_factors[j].append(i)
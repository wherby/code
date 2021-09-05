def factorize(n):
    '''Adapted from http://www.math.utah.edu/~carlson/notes/python.pdf'''
    if n < 2:
        return []
    d = 2
    factors = []
    while not n % d:
        factors.append(d)
        n /= d
    d = 3
    while n > 1 and d * d <= n:
        if not n % d:
            factors.append(d)
            n /= d
        else:
            d += 2
    if n > 1:
        factors.append(n)
	return factors

print factorize(100)
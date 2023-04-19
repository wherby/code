

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad13d
# https://brilliant.org/wiki/extended-euclidean-algorithm/


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

print(egcd(1432,123211))
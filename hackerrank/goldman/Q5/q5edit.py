
from math import log

def assert_range(n, minv, maxv):
    assert minv <= n <= maxv

MINN = 3
MAXN = 20
MINX = 1
MAXX = 10**3
MINM = 2
MAXM = 10**9
MINV = 1
MAXV = 10

POWERS = [2,3,5,7]
LOGS = [log(p, 2) for p in POWERS]

def create_empty_data():
    return [0, 0, 0, 0]

def create_data(n):
    data = create_empty_data()
    for i, p in enumerate(POWERS):
        while n % p == 0:
            data[i] += 1
            n /= p
    return data

def mult(a, b):
    assert a is not None
    assert b is not None
    data = [0,0,0,0]
    for i, (x, y) in enumerate(zip(a, b)):
        data[i] = x+y
    return data

def as_exp2(data):
    res = 0
    for i, (p, logval) in enumerate(zip(POWERS, LOGS)):
        res += data[i] * logval
    return res


n = int(raw_input())
assert_range(n, MINN, MAXN);

x, s, f, m = map(int, raw_input().strip().split())
assert_range(x, MINX, MAXX);
assert_range(s, 0, n-1);
assert_range(f, 0, n-1);
assert_range(m, MINM, MAXM);

rates = [[None for _ in xrange(n)] for _ in xrange(n)]

for i in xrange(n):
    for j, rate in enumerate(map(int, raw_input().split())):
        if i == j:
            assert rate == 0
        else:
            assert_range(rate, MINV, MAXV)
            rates[i][j] = create_data(rate)
#print rates
def comb(a, b):
    c = [[None for _ in xrange(n)] for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                if a[i][k] is None or b[k][j] is None:
                    continue
                cur_res = mult(a[i][k], b[k][j])
                cur_exp = as_exp2(cur_res)
                if c[i][j] is None or cur_exp > as_exp2(c[i][j]):
                    c[i][j] = cur_res
    return c

def solve(m):
    if m == 1:
        return rates
    if m % 2 == 0:
        half = solve(m/2)
        return comb(half, half)
    return comb(solve(m-1), rates)

mat = solve(m)
res = mat[s][f]

MOD = 10**9+7
for i, p in enumerate(POWERS):
    x *= pow(p, res[i], MOD)
    x %= MOD
print x
#print mat
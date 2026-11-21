# https://codeforces.com/gym/106788/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1102/solution/cf106788b.md
# 这里实现双模HASH，这里有个注意的问题是在基数pw选取的时候，需要选一个大于集合最大值的数字
# rdn 模数和基数只要互质就可以，所以在字符串HASH 的时候，只需要设置基数是131即可


import init_setting
from cflibs import *


def main():
    n, k = MII()

    pw = random.randint(10**6, 2 * 10**6)

    def gen():
        while True:
            x = random.getrandbits(40)
            if math.gcd(x, pw) == 1:
                return x

    rnd1 = gen()
    rnd2 = gen()

    pw1 = [1] * (k + 1)
    pw2 = [1] * (k + 1)

    for i in range(k):
        pw1[i + 1] = pw1[i] * pw % rnd1
        pw2[i + 1] = pw2[i] * pw % rnd2

    p = list(range(k))

    v1 = 0
    v2 = 0

    for i in range(k):
        v1 += pw1[i] * p[i]
        v2 += pw2[i] * p[i]

        v1 %= rnd1
        v2 %= rnd2

    cnt = Counter()
    cnt[(v1, v2)] = 1

    ans = 0

    for _ in range(n):
        x, y = GMI()

        v1 += (p[y] - p[x]) * (pw1[x] - pw1[y])
        v1 %= rnd1

        v2 += (p[y] - p[x]) * (pw2[x] - pw2[y])
        v2 %= rnd2

        p[x], p[y] = p[y], p[x]

        ans += cnt[(v1, v2)]
        cnt[(v1, v2)] += 1

    print(ans)

# https://codeforces.com/problemset/problem/442/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0409/solution/cf442a.md
# 列举所有的空间状态，对cur进行染色编码，最终看vis里记录了的染色状态

from cflibs import *

def main():
    n = II()
    s = LI()
    s = list(set(s))
    n = len(s)

    d = {}
    d['R'] = 0
    d['G'] = 1
    d['B'] = 2
    d['Y'] = 3
    d['W'] = 4

    ans = 10000

    for msk1 in range(32):
        for msk2 in range(32):
            vis = set()
            for i in range(n):
                cur = 0
                if msk1 >> d[s[i][0]] & 1:
                    cur += (d[s[i][0]] + 1) * 10
                if msk2 >> (int(s[i][1]) - 1) & 1:
                    cur += int(s[i][1])
                vis.add(cur)
            if len(vis) == n:
                ans = fmin(ans, msk1.bit_count() + msk2.bit_count())

    print(ans)
main()

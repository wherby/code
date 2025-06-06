# https://codeforces.com/problemset/problem/529/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0602/solution/cf529b.md
# 这里求H 的可能值，可以用所有可能的H测试，先求在H固定的时候不得不选择倒转的值，然后贪婪求W最小的选择

import sys
sys.path.append("..")
from cflibs.cflibs import *

def main():
    n = II()
    ws = []
    hs = []

    for _ in range(n):
        w, h = MII()
        ws.append(w)
        hs.append(h)

    st_range = sorted(range(n), key=lambda x: hs[x] - ws[x])

    ans = 10 ** 9 * 2
    used = [0] * n

    cur = sum(ws)

    for h in range(1, 1001):
        flg = True
        cnt = 0
        cur_w = cur
        
        for i in st_range:
            if hs[i] > h:
                if ws[i] > h:
                    flg = False
                    break
                else:
                    used[i] = 1
                    cnt += 1
                    cur_w += hs[i] - ws[i]
            else:
                used[i] = 0
        
        if cnt * 2 > n or not flg: continue
        
        for i in st_range:
            if not used[i] and cnt < n // 2 and ws[i] <= h and hs[i] - ws[i] < 0:
                cnt += 1
                cur_w += hs[i] - ws[i]

        ans = fmin(ans, cur_w * h)

    print(ans)
# https://codeforces.com/problemset/problem/375/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0502/solution/cf375b.md
# 用cur[i]记录当前列的最大往左的长度
from cflibs import *
def main():
    n, m = MII()
    grid = [[int(c) for c in I()] for _ in range(n)]

    cur = [0] * n
    cnt = [0] * (m + 1)

    ans = 0

    for j in range(m):
        for i in range(n):
            cur[i] = cur[i] + 1 if grid[i][j] else 0
        # print(j)
        # print(cur)
        for x in cur:
            cnt[x] += 1
        # print(cnt)
        c = 0
        for i in range(m, -1, -1):
            c += cnt[i]
            ans = fmax(ans, c * i)

        for x in cur:
            cnt[x] -= 1

    print(ans)

main()

# https://codeforces.com/problemset/problem/12/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0509/solution/cf12e.md
from cflibs import *
def main():
    n = 6

    ans = [[0] * n for _ in range(n)]

    for i in range(n - 1):
        for j in range(n - 1):
            ans[i][j] = (i + j) % (n - 1) + 1
    print('\n'.join(' '.join(map(str, x)) for x in ans))
    print('\n')

    for i in range(n):
        ans[-1][i] = ans[i][i]
        ans[i][-1] = ans[i][i]
        ans[i][i] = 0

    print('\n'.join(' '.join(map(str, x)) for x in ans))

main()
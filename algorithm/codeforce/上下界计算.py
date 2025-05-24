

# https://codeforces.com/problemset/problem/1080/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0521/solution/cf1080d.md
from cflibs import *
def main():
    t = II()
    outs = []

    f = [0]

    for _ in range(31):
        f.append(4 * f[-1] + 1)

    for _ in range(t):
        n, k = MII()
        if n > 31: outs.append(f'YES {n - 1}')
        else:
            for i in range(n):
                cuts = n - i
                left = (1 << cuts + 1) - 2 - cuts
                right = f[n] - ((1 << cuts + 1) - 1) * f[i]
                if left <= k <= right:
                    outs.append(f'YES {i}')
                    break
            else:
                outs.append('NO')

    print('\n'.join(outs))
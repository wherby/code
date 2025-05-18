# https://codeforces.com/problemset/problem/309/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0516/solution/cf309b.md
import sys
sys.path.append("..")
from cflibs.cflibs import *
from cflibs import *


def main():
    n, r, c = MII()
    strs = LI()
    lens = [len(x) for x in strs]

    notes = [0] * (n + 1)

    left, right = 0, 0
    total = 0

    while left < n:
        while right < n and right - left + total + lens[right] <= c:
            total += lens[right]
            right += 1
        
        notes[left] = right
        total -= lens[left]
        left += 1

    notes[n] = n

    tmp = notes[:]
    cur = list(range(n + 1))

    for i in range(20):
        if r >> i & 1:
            cur = [tmp[i] for i in cur]
        tmp = [tmp[i] for i in tmp]

    ans, idx = -1, -1
    for i in range(n):
        if cur[i] - i > ans:
            ans = cur[i] - i
            idx = i

    res = []
    for _ in range(r):
        if notes[idx] > idx:
            res.append(' '.join(strs[idx:notes[idx]]))
            idx = notes[idx]

    print('\n'.join(res))
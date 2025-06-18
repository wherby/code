# https://codeforces.com/problemset/problem/254/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0616/solution/cf254c.md
# 获取替换之后的最小字典序，如果是大的就延迟做，如果小就尽快做，延迟的贪心是选择最后需要被替换的数量

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    fin = open('input.txt', 'r')
    input = lambda: fin.readline().strip()

    fout = open('output.txt', 'w')
    print = lambda x: fout.write(x + '\n')

    s1 = [ord(c) - ord('A') for c in I()]
    s2 = [ord(c) - ord('A') for c in I()]

    cnt1 = [0] * 26
    for c in s1:
        cnt1[c] += 1

    cnt2 = [0] * 26
    for c in s2:
        cnt2[c] += 1

    n = len(s1)
    ans = 0

    v1 = [0] * 26
    v2 = [0] * 26

    for i in range(26):
        v = abs(cnt1[i] - cnt2[i])
        if cnt1[i] > cnt2[i]: v1[i] = v
        else: v2[i] = v
        ans += v

    for i in range(n):
        cnt1[s1[i]] -= 1
        
        if v1[s1[i]]:
            for j in range(26):
                if j >= s1[i] and cnt1[s1[i]] >= v1[s1[i]]: break
                if v2[j]:
                    v1[s1[i]] -= 1
                    v2[j] -= 1
                    s1[i] = j
                    break

    print(str(ans // 2))
    print(''.join(chr(ord('A') + c) for c in s1))
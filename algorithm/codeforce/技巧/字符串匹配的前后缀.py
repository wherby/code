# https://codeforces.com/problemset/problem/223/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0729/solution/cf223b.md
#A: abacaba
#B:  aba 
#求是否用A中的任意一个字母构建的子序列能否构成B
# 用前后缀计算： 后缀数列记录到 i位置，最多可以匹配的B的后缀位置
#              前缀记录当前最多匹配的B的前缀位置，但是由于一定要用当前值，所以同时记录当前字母在B出现的前缀最后一个位置，因为以当前值为结尾的子序列只能匹配到前缀数列中的同一字母结束的最长序列


import init_setting
from cflibs import *
def main():
    s1 = [ord(c) - ord('a') for c in I()]
    n1 = len(s1)

    s2 = [ord(c) - ord('a') for c in I()]
    n2 = len(s2)

    suff = [n2] * (n1 + 1)

    for i in range(n1 - 1, -1, -1):
        suff[i] = suff[i + 1]
        if suff[i] > 0 and s1[i] == s2[suff[i] - 1]:
            suff[i] -= 1

    pt = 0
    last_c = [-2] * 26

    for i in range(n1):
        if pt < n2 and s1[i] == s2[pt]:
            last_c[s1[i]] = pt
            pt += 1
        
        if suff[i + 1] > last_c[s1[i]] + 1:
            exit(print('No'))

    print('Yes')
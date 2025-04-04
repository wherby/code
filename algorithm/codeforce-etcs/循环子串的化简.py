# https://codeforces.com/problemset/problem/1090/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0402/solution/cf1090k.md
# 利用循环子串s2对s1进行化简 提取特征值
import sys
sys.path.append("..")
from cflibs.cflibs import *

def main():
    t = II()
    vis = defaultdict(list)

    for idx in range(1, t + 1):
        s1, s2 = LI()
        
        l1 = [ord(c) - ord('a') for c in s1]
        l2 = [ord(c) - ord('a') for c in s2]
        
        msk = 0
        for c in l2:
            msk |= 1 << c
        
        i = len(l1) - 1
        while i >= 0 and msk >> l1[i] & 1:
            i -= 1
        
        s1 = s1[:i + 1]
        vis[(msk, s1)].append(idx)

    print(len(vis))
    outs = []

    for x in vis.values():
        outs.append(f'{len(x)} {" ".join(map(str, x))}')

    print('\n'.join(outs))
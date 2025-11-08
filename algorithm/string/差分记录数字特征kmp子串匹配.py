# https://codeforces.com/gym/106159/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1107/solution/cf106159d.md
# 使用差分记录子串特征，kmp做子串匹配



import init_setting
from cflibs import *
def main(): 
    def prep(p):
        pi = [0] * len(p)
        j = 0
        for i in range(1, len(p)):
            while j != 0 and p[j] != p[i]:
                j = pi[j - 1]
            if p[j] == p[i]:
                j += 1
            pi[i] = j
        return pi
    
    M = 10 ** 4
    
    n, m = MII()
    nums1 = LII()
    nums2 = LII()
    
    vals = []
    
    for i in range(1, m):
        vals.append((nums2[i] - nums2[i - 1]) % M)
    
    vals.append(-1)
    
    for i in range(1, n):
        vals.append((nums1[i] - nums1[i - 1]) % M)
    
    kmp = prep(vals)
    
    cnt = [0] * M
    
    for i in range(m, n + m - 1):
        if kmp[i] == m - 1:
            cnt[(nums2[0] - nums1[i - 2 * (m - 1)]) % M] += 1
    
    ma = max(cnt)
    print(cnt.index(ma), ma)
# https://codeforces.com/gym/106642/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0814/solution/cf106642a.md
# 这里有N个子字符串排列成循环字符串，求 pattern 串出现的最大次数
# 除了第一个子串因为循环移动会截取成两个串，中间的子串都是完整的，所以可以用状态压缩求 dp[i][j][msk] i表示从i-index开始 到j-index 的时候用了msk子串 里有多少个完整的pattern
# 然后加上 可能的特色子串的前后缀计算
# algorithm/codeforce/dp/docs/循环前后缀的状态压缩.md
# 首先计算每个字符串的KMP转换
# algorithm/string/kmp/KMP转移矩阵.md

import init_setting
from cflibs import *
def main():
    n = II()
    strs = [[ord(c) - ord('a') for c in I()] for _ in range(n)]
    pattern = [ord(c) - ord('a') for c in I()]
    
    k = len(pattern)
    transition = [[0] * 26 for _ in range(k + 1)]
    
    for i in range(k + 1):
        for j in range(26):
            tmp = []
            for idx in range(i):
                tmp.append(pattern[idx])
            tmp.append(j)
            
            l = len(tmp)
            for cur_len in range(fmin(l, k), -1, -1):
                flg = True
                
                for idx in range(cur_len):
                    if pattern[idx] != tmp[l - cur_len + idx]:
                        flg = False
                
                if flg:
                    transition[i][j] = cur_len
                    break
    
    transition_string = [[None] * (k + 1) for _ in range(n)]
    
    for i in range(n):
        for j in range(k + 1):
            cur = j
            cnt = 0
            
            for c in strs[i]:
                cur = transition[cur][c]
                if cur == k: cnt += 1
            
            transition_string[i][j] = (cur, cnt)
    
    def f(x, y):
        return x * (k + 1) + y
    
    dp = [[-1] * (1 << n) for _ in range((k + 1) * (k + 1))]
    
    for i in range(k + 1): dp[f(i, i)][0] = 0
    
    for msk in range(1 << n):
        for i in range(k + 1):
            for j in range(k + 1):
                if dp[f(i, j)][msk] != -1:
                    for bit in range(n):
                        if msk >> bit & 1: continue
                        nmsk = msk | (1 << bit)
                        nj, ncnt = transition_string[bit][j]
                        dp[f(i, nj)][nmsk] = fmax(dp[f(i, nj)][nmsk], dp[f(i, j)][msk] + ncnt)
    
    ans = 0
    
    for i in range(n):
        l = len(strs[i])
        
        for j in range(l):
            cur, cnt = 0, 0
            
            for idx in range(j, l):
                cur = transition[cur][strs[i][idx]]
                if cur == k: cnt += 1
            
            msk = (1 << n) - 1 - (1 << i)
            for ncur in range(k + 1):
                if dp[f(cur, ncur)][msk] != -1:
                    ncnt = cnt + dp[f(cur, ncur)][msk]
                    
                    for idx in range(j):
                        ncur = transition[ncur][strs[i][idx]]
                        if ncur == k: ncnt += 1
                    
                    ans = fmax(ans, ncnt)
    
    print(ans)
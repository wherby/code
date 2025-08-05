# https://codeforces.com/problemset/problem/163/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0801/solution/cf163a.md
# 在s1中选择子串 与在s2中选择子序列，求两者相等的数量
# DP[i+1][j+1] 表示以 i-idex为结尾子串S1  与S2[:j]状态的数量
# 为什么S1在外层，S2在内层？ 
# 因为这里其实不能求出到底相等的字符串是多少长度，只是状态从一个状态到另一个状态转移的时候，值是多少
# 因为S1是子串，所以遍历S1中结尾子串，与S2中对比，如果匹配，则转换到上一个状态就好了， 对于每个不同子串结束的 S1，DP初始值可以从0 开始计算 DP[i][0] = 0 
# 



import init_setting
from lib.cflibs import *
def main():
    s1 = [ord(c) for c in I()]
    s2 = [ord(c) for c in I()]
    
    n1 = len(s1)
    n2 = len(s2)
    
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    
    mod = 10 ** 9 + 7
    ans = 0
    
    for i in range(n1):
        dp[i][0] = 1
        
        for j in range(n2):
            dp[i][j + 1] += dp[i][j]
            if dp[i][j + 1] >= mod:
                dp[i][j + 1] -= mod
            
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] += dp[i][j]
                if dp[i + 1][j + 1] >= mod:
                    dp[i + 1][j + 1] -= mod
                
                ans += dp[i][j]
                if ans >= mod:
                    ans -= mod
    
    print(ans)
# https://codeforces.com/gym/104736/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0223/solution/cf104736i.md
# 块内贡献和块间贡献分开计算，
# 块间贡献的时候，不需要考虑块内同一字符的分布，只需遍历块内当前字符，找到当前字符的贡献。这样就能计算出块内每个字符的贡献了


import init_setting
from cflibs import *
def main(): 
    s = I()
    n = II()
    mod = 10 ** 9 + 7
    
    n %= mod
    
    ans = 0
    cnt = [0] * 26
    
    for c in s:
        ch = ord(c) - ord('a')
        
        for i in range(ch + 1, 26):
            ans += cnt[i]
        
        cnt[ch] += 1
    
    ans = n * ans % mod
    
    for i in range(26):
        for j in range(i):
            ans += n * (n - 1) // 2 % mod * cnt[i] % mod * cnt[j] % mod
            ans %= mod
    
    print(ans)
# https://codeforces.com/gym/103464/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0912/solution/cf103464c.md
# 这个题目中完全不一致，也是完全一致，就是中心对称回文的类似算法，所以可以用manacher的框架解决


import init_setting
from cflibs import *
def main():
    n = II()
    s = [ord(c) - ord('a') for c in I()]
    
    manacher = [0] * (n - 1)
    
    ans = 0
    chosen_idx = 0
    
    for i in range(n - 1):
        if chosen_idx + manacher[chosen_idx] >= i and 2 * chosen_idx >= i:
            manacher[i] = fmin(manacher[2 * chosen_idx - i], chosen_idx + manacher[chosen_idx] - i)
        
        l = i - manacher[i] + 1
        r = i + manacher[i]
        
        while l > 0 and r + 1 < n and s[l - 1] != s[r + 1]:
            l -= 1
            r += 1
            manacher[i] += 1
        
        if i + manacher[i] > chosen_idx + manacher[chosen_idx]:
            chosen_idx = i
    
    print(max(manacher) * 2)

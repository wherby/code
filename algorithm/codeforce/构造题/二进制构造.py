# https://codeforces.com/gym/106782/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1026/solution/cf106782d.md


import init_setting
from cflibs import *
def main():
    n = II()
    
    def solve(n):
        if n == 0: return []
        tmp = [x + 1 for x in solve(n - 1)] + [1]
        return tmp * 2
    
    ans = solve(n)
    
    print(len(ans))
    print(' '.join(map(str, ans)))
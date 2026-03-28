# https://codeforces.com/gym/103439/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0324/solution/cf103439j.md
# 需要知道是否可以改变一次就能成功，就是两边的和能同时有两个指标符合，所以使用双指针计算挖去中间之后余下的数量，遍历挖去左，移动右的方式取得是否能满足两个条件
# 要计算挖去中间，需要先用右指针作为减去，左指针作为加入，和平时计算相反


import init_setting
from cflibs import *
def main(): 
    n = II()
    s = I()
    
    ca = s.count('A')
    cb = s.count('B')
    cc = s.count('C')
    
    if ca == n and cb == n and cc == n: print(0)
    else:
        l = 0
        r = 0
        
        while l < 3 * n:
            while max(ca, cb, cc) > n and r < 3 * n:
                if s[r] == 'A': ca -= 1
                elif s[r] == 'B': cb -= 1
                else: cc -= 1
                r += 1
            
            if max(ca, cb, cc) > n: break
            
            if ca == n and cb == n:
                print(1)
                print(l + 1, r, 'C')
                exit()
            
            if ca == n and cc == n:
                print(1)
                print(l + 1, r, 'B')
                exit()
            
            if cb == n and cc == n:
                print(1)
                print(l + 1, r, 'A')
                exit()
            
            if s[l] == 'A': ca += 1
            elif s[l] == 'B': cb += 1
            else: cc += 1
            l += 1
        
        ca = 0
        cb = 0
        cc = 0
        
        print(2)
        for i in range(3 * n):
            if s[i] == 'A': ca += 1
            elif s[i] == 'B': cb += 1
            else: cc += 1
            
            if ca == n:
                print(i + 2, 3 * n, 'B')
                print(3 * n - (n - cc) + 1, 3 * n, 'C')
                break
            
            if cb == n:
                print(i + 2, 3 * n, 'A')
                print(3 * n - (n - cc) + 1, 3 * n, 'C')
                break
            
            if cc == n:
                print(i + 2, 3 * n, 'A')
                print(3 * n - (n - cb) + 1, 3 * n, 'B')
                break
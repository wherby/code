# https://codeforces.com/gym/106501/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0428/solution/cf106501k.md
# 二分的搜寻效率最高的写法，如果是平时的写法，每次筛除n//2个数字，在满足条件的时候，对mid这个值要log(n)才能筛查出来，这种写可以每次都去除 (n+1)//2个数字，其实效率不会差太多，
# 但是如果testcase设计到刚好mid位置就会差很多



import init_setting
from cflibs import *
def main():
    def query(l, r):
        print('?', l + 1, r + 1, flush=True)
        return II()
    
    def answer(p):
        print('!', p + 1)
    
    n = II()
    
    if query(0, 0):
        answer(0)
    else:
        block = 1
        l_bound = 1
        r_bound = 1
        for i in range(1, 30):
            r = 1 << i
            l = r // 2
            
            if r >= n:
                r_bound = n - 1
                break
            
            block = r - l
            if query(l, r - 1):
                r_bound = r - 1
                break
            
            l_bound = r
        
        l = l_bound
        r = r_bound
        
        while l <= r:
            mid = (l + r) // 2
            if query(mid - block + 1, mid): r = mid - 1
            else: l = mid + 1
        
        answer(l)
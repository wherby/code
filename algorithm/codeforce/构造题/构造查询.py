# https://codeforces.com/gym/100488/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0930/solution/cf100488b.md
# 因为题目的查询数目是(n+1)//2，如果二分的话，在小数字的时候是会大于这个值，
#  对于奇数的情况，先变偶数，然后偶数先分半，然后每次查询确定首尾

import init_setting
from lib.cflibs import *
def main():
    def query(l, r):
        print('Q', l, r, flush=True)
        return LII()
    
    def answer(nums):
        print('A', *nums, flush=True)
    
    n = II()
    
    ans = [0] * n
    to_find = set(range(1, n + 1))
    
    if n % 2:
        ans[n - 1] = query(n, n)[0]
        to_find.remove(ans[n - 1])
        n -= 1
    
    if n:
        left = set(query(1, n // 2))
        right = to_find - left
        
        for i in range(2, n // 2 + 1):
            mid = set(query(i, n + 1 - i))
            ans[i - 2] = (left - mid).pop()
            ans[n - i + 1] = (right - mid).pop()
            
            left &= mid
            right &= mid
        
        ans[n // 2 - 1] = left.pop()
        ans[n // 2] = right.pop()
    
    answer(ans)
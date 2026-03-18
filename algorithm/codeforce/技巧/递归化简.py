# https://codeforces.com/gym/106415/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0313/solution/cf106415f.md
# 递归简化，在solve函数里，每次可以减少至少一位，所以最后一定能得到相等的数字




import init_setting
from cflibs import *
def main(): 
    def query(a, b):
        print('?', a, b, flush=True)
        return int(LI()[1])
    
    def answer(x):
        print('!', x, flush=True)
        return I()
    
    def solve(x):
        if x & -x == x:
            return query(x, x) // 2
        v = 1 << x.bit_length()
        return query(v - x, x) - solve(v - x)
    
    n = II()
    nums = LII()
    
    for x in nums:
        answer(solve(x))
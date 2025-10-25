# https://codeforces.com/gym/103886/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1020/solution/cf103886g.md
# “偶数”在前，“奇数” 在后迭代构造使得数组不能有“等差”数列
#


import init_setting
from cflibs import *
def main(): 
    def solve(x):
        if x == 1: return [1]
        even = x // 2
        odd = x - x // 2
        return [x * 2 for x in solve(even)] + [x * 2 - 1 for x in solve(odd)]
    
    n = II()
    print(*solve(n))
    ls = solve(n)
    print([bin(a) for a in ls])

main()
# https://codeforces.com/problemset/problem/2071/D1
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0826/solution/cf2071d1.md
# 这个题目只求了一个点的值
# 这里用小数组生成的循环数组是有特性，相邻两位生成的数字相等
# 如果原数组是奇数个数字，先计算下一个数字，补充到偶数个数字
# 按照定义如果长度大于n*2， 则可以知道最后的值是 [a1...an]+ [an+1,an+2]...av
# 如果av是偶数，则它还存在，加上前面的[a1,,an]


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, l, r = MII()
        nums = LII()
        
        if n % 2 == 0:
            v = 0
            for i in range(n // 2):
                v ^= nums[i]
            nums.append(v)
            n += 1
        
        total = reduce(xor, nums)
        
        def solve(x):
            if x <= n: return nums[x - 1]
            
            if x <= 2 * n:
                ans = 0
                for i in range(x // 2):
                    ans ^= nums[i]
                return ans
            
            v = x // 2
            if v % 2 == 0: return total ^ solve(v) 
            return total
        
        outs.append(solve(l))
    
    print('\n'.join(map(str, outs)))

main()
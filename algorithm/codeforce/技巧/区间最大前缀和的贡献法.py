# https://codeforces.com/gym/105056/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1204/solution/cf105056e.md
# 原题是在数组里求任意子数组 的最大前缀和
# 这时用单调栈的方式，遍历子数组结束为i的数组，得到当前数字的acc 可以影响到最右的位置为贡献值，加上上一个数的贡献值作为结尾为r > i 的子数组的贡献值
# 减去 (n + 1 - i) * acc[i]  这里表示L =i的时候，【0，L-1】位置的前缀和对最大前缀和的影响
# 其实可以看成两个子数组相减， 


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
    
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + nums[i]
    
        ans = 0
    
        stk = [n + 1]
        stk_acc = [0]
        
        for i in range(n, -1, -1):
            while stk[-1] != n + 1 and acc[i] >= acc[stk[-1]]:
                stk_acc.pop()
                stk.pop()
            
            stk_acc.append(stk_acc[-1] + (stk[-1] - i) * acc[i])
            stk.append(i)
            
            ans += stk_acc[-1] - (n + 1 - i) * acc[i]  # L =i 的影响值 这时L=i ,R = i ...n  有n-i+1 个
    
    print('\n'.join(map(str, outs)))

main()
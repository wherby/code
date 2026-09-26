# https://codeforces.com/gym/106642/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0812/solution/cf106642j.md
# algorithm/codeforce/dp/docs/单调栈DP贡献累加.md
# 这里是基于单调栈的DP贡献累加。从右到左看，区间最小值一定是递减的，所以每次栈内滞留的最小值对应的奇数个数在新的右端点都是成立的，所以需要cur累积当前栈内奇数个最小子数组个数
# 这里DP发生在每次增加一个新的右端点：
# 如果次端点小于栈顶元素，则栈顶的最小值就不能在此时有影响力了，需要把栈顶弹出，并且把累加值去除
# 如果是新的最小值，则把当前的最小值形成的影响力状态入栈
# 如果是等于栈顶， 则此时栈顶的状态奇偶性发生了改变， 需要先把奇数个影响力从当前去除
#        前面状态的奇数个子数组个数 加上当前元素变成了偶数个原数个数
#        而奇数个元素个数则不是偶数个元素个数变化而来，还多了一个0个当前数字转换来的，i-idx 则表示前面没有当前元素的个数
# 栈中元素 [(-inf, -1, 0, 0)] 表示 从当前元素的最小值，最小值出现的位置， 奇数个最小值的子数组数， 偶数个最小值的子数组个数


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        ans = 0
        cur = 0
    
        stk = [(-inf, -1, 0, 0)]
        
        for i in range(n):
            while stk[-1][0] > nums[i]:
                cur -= stk[-1][2]
                stk.pop()
            
            if stk[-1][0] != nums[i]:
                stk.append((nums[i], i, i - stk[-1][1], 0))
            else:
                val, idx, dp1, dp2 = stk.pop()
                cur -= dp1
                stk.append((nums[i], i, dp2 + i - idx, dp1))
            
            cur += stk[-1][2]
            ans += cur
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))
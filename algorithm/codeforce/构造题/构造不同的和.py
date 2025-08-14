# 
# https://codeforces.com/problemset/problem/856/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0808/solution/cf856a.md
# 已知数组A由不同的数字组成， 构造同样的长度的数组B，使得任意 ai+bj 的值不相等
# 思考： 为什么B数组第一个数字可以填1

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    M = 10 ** 6 + 1
    used = [0] * M
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        ans = []
        
        for i in range(1, M):
            if not used[i]:
                used[i] = 1
                ans.append(i)
                
                for j in range(n):
                    for k in range(j):
                        v = i + abs(nums[j] - nums[k])
                        if v < M:
                            used[v] = 1
                
                if len(ans) == n:
                    break
        
        for i in range(M):
            used[i] = 0
        
        outs.append('YES')
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))
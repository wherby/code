# https://codeforces.com/gym/106760/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1013/solution/cf106760e.md
# 如果按照index分析的时候，坐标左右移会有(+1,0,-1)三种状态。
# 按照值的顺序，就可以不用考虑当前点是左移还是右移，因为需要当前点的值更大，所以只能是当前点右移才可以，然而当前点右移能增大的前提是当前点的下一个点比当前点先计算，即就是按照值的先后顺序来说是较小数字。所以值域分析的时候从小到大遍历值域情况，只需要关心后一个数字是否已经被遍历到了，就可以完成线段树LIS计算
# algorithm/advancedDS/值域分析/线段树值域分析.md
# 值域分析
# dp0 表示当前位置没有交换的最大值，


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        pos = [0] * (n + 1)
        for i in range(n):
            pos[nums[i]] = i
        
        dp0 = [0] * n
        
        seg = SegTree(fmax, 0, n)
        
        for i in range(1, n + 1):
            p = pos[i]
            
            dp0[p] = seg.prod(0, p) + 1
            
            v = dp0[p]
            if p + 1 < n and nums[p] > nums[p + 1]:
                v = fmax(v, dp0[p + 1] + 1)
            
            seg.set(p, v)
        
        outs.append(f'{seg.all_prod()}')
    
    print('\n'.join(outs))
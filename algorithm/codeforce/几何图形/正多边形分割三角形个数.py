# https://codeforces.com/problemset/problem/1942/C2
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0723/solution/cf1942c2.md
# 因为正N变形，最多可以分割N-2个三角型， 原始题目已经标记X个点，等于把正多边形变成了X个凸边型，
# 对与M个凸边型，如果间隔标记，每次标记会多2个三角形，如果(M-2)是奇数的时候，最后一次标记会多3个三角形，所以奇数的凸四边形要先标记，
# 奇数情况下,可以用(M-2)//2个标记点得到为 M-2个三角形， 所以奇数小的应该先标记以获取最大增益
# 就是剩余标记每次都可以多2个三角形  《= 这里是因为如果是偶数情况，需要考虑如果正M型，M=2的时候，需要把两个M=2的合成之后变成两个三角形，这些复杂情况，所以就直接求理论上界，这个上届会比N-2的实际上届大
# 但是最多的标记数目是N-2,如果计算出的数目大于N-2也只能取N-2
# 


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, x, y = MII()
        nums = LII()
        nums.sort()
        
        vs = []
        cnt = x
        
        for i in range(1, x):
            v = nums[i] - nums[i - 1] - 1
            if v % 2:
                vs.append(v)
        
        v = nums[0] + n - nums[-1] - 1
        if v % 2:
            vs.append(v)
        
        vs.sort()
        for x in vs:
            if y >= x // 2:
                y -= x // 2
                cnt += x
    
        cnt = fmin(n, cnt + y * 2)
        outs.append(cnt - 2)
    
    print('\n'.join(map(str, outs)))
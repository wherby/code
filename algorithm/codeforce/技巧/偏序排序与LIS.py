# https://codeforces.com/gym/106443/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0331/solution/cf106443h.md
# 这里为什么会用 (y-x,y+x) 作为偏序排序的key，然后用LIS来计算可能值
# y-x表示人运动到y点之后的剩余时间，这里肯定只能从小到大，而y+x则从约束的绝对值展开得到的 algorithm/codeforce/docs/绝对值展开偏序排序与Lis.md
# 这里使用python sort是稳定的特性实现了偏序排序
    # st_range.sort(key=lambda x: ys[x])
    # st_range.sort(key=lambda x: xs[x])

import init_setting
from cflibs import *
def main(): 
    n = II()
    xs = []
    ys = []
    
    for _ in range(n):
        x, y = MII()
        if y - x >= 0:
            xs.append(y - x)
            ys.append(y + x)
    
    n = len(xs)
    
    st_range = list(range(n))
    
    st_range.sort(key=lambda x: ys[x])
    st_range.sort(key=lambda x: xs[x])
    
    lis = []
    
    for i in st_range:
        if len(lis) == 0 or lis[-1] <= ys[i]:
            lis.append(ys[i])
        else:
            lis[bisect.bisect_right(lis, ys[i])] = ys[i]
    
    print(len(lis))
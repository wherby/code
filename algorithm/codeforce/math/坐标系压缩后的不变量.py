# https://codeforces.com/gym/104985/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0306/solution/cf104985a.md
# 看似每次下载完成之后的速度都变了，其实把下载完成前和下载完成后两个坐标系来看，就像是把下载完成后的点的坐标系压缩了
# 在题目中的等比变化速度的条件下，下载完成的顺序是不变的，速度在如果变化和保持不变的情况下，前一个下载完成时，后一个剩余的下载量是不变的，只有速度变了，等效于在时间轴上进行了等比例的压缩
# 而如果剩余的量不变的话，则下一个完成的时间 vx*tx = v&t , vx 表示变化后的速度，v表示变化前的速度
# vx/ v = total_v / (total_v - v[i])， 0<=i<x 所以下载完成的顺序不变，等效于在时间轴上进行了等比例的压缩，所以每次下载完成之后的速度变化和保持不变是等价的
# 利用性质求得没一段的新的下载时间，进行累加


import init_setting
from cflibs import *
def main(): 
    n = II()
    vs = []
    ts = []
    
    for _ in range(n):
        v, t = MII()
        vs.append(v)
        ts.append(t)
    
    st_range = sorted(range(n), key=lambda x: ts[x])
    total_v = sum(vs)
    
    res = 0
    
    cur_t = 0
    cur_v = total_v
    
    ans = [0] * n
    
    for i in st_range:
        res += (ts[i] - cur_t) * cur_v / total_v
        cur_t = ts[i]
        cur_v -= vs[i]
        ans[i] = res
    
    print('\n'.join(map(str, ans)))
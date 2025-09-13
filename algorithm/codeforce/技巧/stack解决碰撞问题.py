# https://codeforces.com/gym/101875/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0911/solution/cf101875g.md
# 原问题只需要最后一次碰撞的时间。所以stack 顶记录最近一次碰撞
# 因为碰撞之后，速度就一样了 ，if stk_v[-1] >= v:  这时和最近的物体不会发生碰撞，除非是前一个被碰撞降速，所以前一个点不需要，pop出去
# if (v - v2) * (x - x1) <= (v - v1) * (x - x2): 这时，是前一个点的碰撞时间在当前这个点的碰撞时间之前，所以，当前点的碰撞和前一点无关，只与前2点有关，所以把前一点移除
# stack 记录了凸点


import init_setting
from cflibs import *

def main():
    n = II()
    xs = []
    vs = []
    
    for _ in range(n):
        x, v = MII()
        xs.append(x)
        vs.append(v)
    
    st_range = sorted(range(n), key=lambda x: -xs[x])
    
    stk_x = []
    stk_v = []
    
    ans = 0
    
    for i in st_range:
        x, v = xs[i], vs[i]
        
        while len(stk_x):
            if stk_v[-1] >= v: 
                stk_x.pop()
                stk_v.pop()
            elif len(stk_x) > 1:
                x1, v1 = stk_x[-1], stk_v[-1]
                x2, v2 = stk_x[-2], stk_v[-2]
                
                if (v - v2) * (x - x1) <= (v - v1) * (x - x2):
                    stk_x.pop()
                    stk_v.pop()
                else:
                    break
            else:
                break
        
        if len(stk_x):
            x1, v1 = stk_x[-1], stk_v[-1]
            ans = fmax(ans, -(x - x1) / (v - v1))
    
        stk_x.append(x)
        stk_v.append(v)
    
    print(ans)
# https://codeforces.com/contest/2206/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0713/solution/cf2206j.md
# 使用互逆函数，同时记录值所在位置和位置上的值 ： algorithm/codeforce/docs/basic/双向指针互逆函数.md
# if idx1 + 1 != idx2: 这里防止重合路径计算，并且在前面做了排序去除重合路径的组合


import init_setting
from cflibs import *
def main():
    n, q = MII()
    p1 = LGMI()
    p2 = LGMI()
    
    pos1 = [0] * n
    pos2 = [0] * n
    
    for i in range(n): pos1[p1[i]] = i
    for i in range(n): pos2[p2[i]] = i
    
    def cost(idx):
        if idx <= 0 or idx >= n: return 0
        x, y = p2[idx - 1], p2[idx]
        px = pos1[x]
        py = pos1[y]
        return (py - px) % n - 1
    
    def calc(idx1, idx2):
        if idx1 > idx2: idx1, idx2 = idx2, idx1
        ans = 0
        ans += cost(idx1)
        ans += cost(idx1 + 1)
        
        if idx1 + 1 != idx2:
            ans += cost(idx2)
        ans += cost(idx2 + 1)
        return ans
    
    ans = 0
    for i in range(1, n):
        ans += cost(i)
    
    outs = [ans + pos1[p2[0]]]
    
    for _ in range(q - 1):
        c, x, y = GMI()
        
        if c == 0:
            ans -= calc(pos2[p1[x]], pos2[p1[y]])
            
            p1[x], p1[y] = p1[y], p1[x]
            pos1[p1[x]], pos1[p1[y]] = pos1[p1[y]], pos1[p1[x]]
            
            ans += calc(pos2[p1[x]], pos2[p1[y]])
        
        else:
            ans -= calc(x, y)
            
            p2[x], p2[y] = p2[y], p2[x]
            pos2[p2[x]], pos2[p2[y]] = pos2[p2[y]], pos2[p2[x]]
            
            ans += calc(x, y)
        
        outs.append(ans + pos1[p2[0]])
    
    print('\n'.join(map(str, outs)))
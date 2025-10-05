# https://codeforces.com/gym/105809/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0927/solution/cf105809c.md
# 在空间中有一个点就不能有另一个点，然后这些点可以奇偶性分组，变成二分图
# 因为有一个点就不能有另一个点，所以可以用最大流来计算这些互相矛盾的点的个数
# 把源连上A点， A点连上矛盾点，然后矛盾点流向汇，流量为1， 这样计算出的最大流就是最大可能矛盾数量
# 


import init_setting
from cflibs import *
from lib.mincostflow import MCFGraph

def main():
    a, b, c = MII()
    blocked = [0] * (a * b * c)
    
    def f(x, y, z):
        return (x * b + y) * c + z
    
    k = II()
    for _ in range(k):
        x, y, z = GMI()
        blocked[f(x, y, z)] = 1
    
    mf = MCFGraph(a * b * c + 2)
    dirs = []
    
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) + abs(j) == 3:
                dirs.append((0, i, j))
                dirs.append((i, 0, j))
                dirs.append((i, j, 0))
    
    cnt = a * b * c
    
    src = a * b * c
    dst = src + 1
    
    for i in range(a):
        for j in range(b):
            for k in range(c):
                if not blocked[f(i, j, k)]:
                    if (i + j + k) % 2 == 0:
                        mf.add_edge(src, f(i, j, k), 1)
                        for di, dj, dk in dirs:
                            ni = i + di
                            nj = j + dj
                            nk = k + dk
                            
                            if 0 <= ni < a and 0 <= nj < b and 0 <= nk < c and not blocked[f(ni, nj, nk)]:
                                mf.add_edge(f(i, j, k), f(ni, nj, nk), 1)
                    else:
                        mf.add_edge(f(i, j, k), dst, 1)
                else:
                    cnt -= 1
    print(cnt - mf.flow(src, dst)[0])

main()

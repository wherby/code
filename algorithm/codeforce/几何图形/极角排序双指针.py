# https://codeforces.com/gym/102829/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1017/solution/cf102829k.md
# 如果枚举平面的所有向量边，然后再枚举每条边同一边点的数量， 这样就是 N**3 的复杂度
# 这里只枚举起点， 然后把所有的边按照极角排序， 再枚举每个边，找到该边对应的同一边点的数量，这样的话复杂度就变成了 N* Nlog(N)
#  if dy > 0 or dy == 0 and dx > 0: pos.append(j)    这里的划分其实也是为了cmp 作准备，同时为了保证两个零点能排在第一位置， 把坐标上的点分为上下两部分
# algorithm/codeforce/几何图形/docs/极角排序.md


import init_setting
from lib.cflibs import *
def main():
    n = II()
    xs = []
    ys = []
    
    mod = 10 ** 9 + 7
    pw2 = [1] * (n + 1)
    
    for i in range(1, n + 1):
        pw2[i] = pw2[i - 1] * 2 % mod
    
    for _ in range(n):
        x, y = MII()
        xs.append(x)
        ys.append(y)
    
    ans = n
    
    for i in range(n):
        pos = []
        neg = []
        
        for j in range(n):
            if j == i: continue
            
            dx = xs[j] - xs[i]
            dy = ys[j] - ys[i]
            
            if dy > 0 or dy == 0 and dx > 0: pos.append(j)
            else: neg.append(j)
        
        def cmp(x, y):
            dx1, dy1 = xs[x] - xs[i], ys[x] - ys[i]
            dx2, dy2 = xs[y] - xs[i], ys[y] - ys[i]
            return -1 if dx1 * dy2 > dy1 * dx2 else 1
        
        pos.sort(key=cmp_to_key(cmp))
        neg.sort(key=cmp_to_key(cmp))
        
        total = pos + neg
        total *= 2
        
        r = 0
        
        for l in range(n - 1):
            r = fmax(r, l + 1)
            
            while r < l + n - 1:
                dx1, dy1 = xs[total[l]] - xs[i], ys[total[l]] - ys[i]
                dx2, dy2 = xs[total[r]] - xs[i], ys[total[r]] - ys[i]
                
                if dx1 * dy2 > dx2 * dy1: r += 1
                else: break
            
            ans += pw2[r - l - 1]
            ans %= mod
    
    print(ans)
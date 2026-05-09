# https://codeforces.com/gym/106414/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0507/solution/cf106414k.md
# algorithm/codeforce/技巧/贪心/局部微调二分图.py  贪心扰动方式
# 要三个特殊点不同，先用两种颜色染色，如果不是都是一种颜色，则用其他颜色替换相同色点即可
# 如果是三个点颜色一致，则只需两个点的距离大于2，就可以把其中一个点置为另一个颜色，然后把另一个点取反然后把邻居点置为2，因为邻居点奇偶性相反，一定不会改动到第3个点


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for _ in range(t):
        n, m = MII()
        pts = []
    
        vis = 0
        
        for _ in range(3):
            x, y = GMI()
            pts.append((x, y))
            vis |= 1 << ((x + y) % 2)
    
        ans = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                ans[i][j] = (i + j) % 2
        
        if vis == 3:
            vis = 0
            
            for x, y in pts:
                if vis >> ((x + y) % 2) & 1:
                    ans[x][y] = 2
                vis |= 1 << ((x + y) % 2)
            
            outs.append('YES')
            
            for x in ans:
                outs.append(''.join('RGB'[i] for i in x))
        
        else:
            flg = False
            
            for i in range(3):
                for j in range(i):
                    x1, y1 = pts[i]
                    x2, y2 = pts[j]
                    
                    if abs(x1 - x2) + abs(y1 - y2) > 2:
                        ans[x1][y1] = 2
                        
                        ans[x2][y2] ^= 1
                        
                        for dx, dy in dirs:
                            if 0 <= x2 + dx < n and 0 <= y2 + dy < m:
                                ans[x2 + dx][y2 + dy] = 2
                        
                        flg = True
                    
                    if flg: break
                if flg: break
            
            if flg:
                outs.append('YES')
                
                for x in ans:
                    outs.append(''.join('RGB'[i] for i in x))
            
            else:
                outs.append('NO')
    
    print('\n'.join(outs))
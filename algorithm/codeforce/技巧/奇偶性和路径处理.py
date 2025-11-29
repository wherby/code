# https://codeforces.com/gym/105712/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1122/solution/cf105712i.md
# 这里有两个难点，第一是奇偶性判断，这里使用奇数位翻转的思路(棋盘问题)，使得得到变换之后奇偶性不变的特性，就可以直接判断两个图形是否等效
# 然后使得每次移动都是从grid1 平面上从1 到0 
# 第二个难点是在x,y轴的移动，为了解决x,y轴上可能不移动的问题，做了判断，但是理论上移动完成之后，再遍历就好了？


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        grid1 = [[1 if c == '#' else 0 for c in I()] for _ in range(n)]
        grid2 = [[1 if c == '#' else 0 for c in I()] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if (i + j) % 2:
                    grid1[i][j] ^= 1
                    grid2[i][j] ^= 1
        
        p1 = []
        p2 = []
        
        for i in range(n):
            for j in range(m):
                if grid1[i][j] != grid2[i][j]:
                    if grid1[i][j]: p1.append((i, j))
                    if grid2[i][j]: p2.append((i, j))
        
        if len(p1) != len(p2): outs.append('-1')
        else:
            ops = []
            
            def go(v1, v2):
                x1, y1 = v1
                x2, y2 = v2
                
                dx = 1 if x2 >= x1 else -1
                dy = 1 if y2 >= y1 else -1
                
                x, y = x1, y1
                cur = [(x1, y1)]
                
                while x != x2:
                    x += dx
                    if grid1[x][y] == 0:
                        cur.append((x, y))
                        for i in range(len(cur) - 1, 0, -1):
                            vx1, vy1 = cur[i]
                            vx2, vy2 = cur[i - 1]
                            grid1[vx1][vy1], grid1[vx2][vy2] = grid1[vx2][vy2], grid1[vx1][vy1]
                            ops.append(f'{vx1 + 1} {vy1 + 1} {vx2 + 1} {vy2 + 1}')
                        cur.clear()
                    cur.append((x, y))
                
                while y != y2:
                    y += dy
                    if grid1[x][y] == 0:
                        cur.append((x, y))
                        for i in range(len(cur) - 1, 0, -1):
                            vx1, vy1 = cur[i]
                            vx2, vy2 = cur[i - 1]
                            grid1[vx1][vy1], grid1[vx2][vy2] = grid1[vx2][vy2], grid1[vx1][vy1]
                            ops.append(f'{vx1 + 1} {vy1 + 1} {vx2 + 1} {vy2 + 1}')
                        cur.clear()
                    cur.append((x, y))
            
            for v1, v2 in zip(p1, p2):
                go(v1, v2)
            
            outs.append(str(len(ops)))
            if ops: outs.append('\n'.join(ops))
    
    print('\n'.join(outs))
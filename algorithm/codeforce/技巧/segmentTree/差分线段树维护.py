# https://codeforces.com/gym/102860/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0605/solution/cf102860l.md
# 每一次翻转只对l,r 内的坐标有影响，其影响相当于叠加了一个直线线段 ax+b， 
# 使用差分线段树标记的方式，记录，然后查询得到当前点的A,B
# algorithm/codeforce/docs/差分线段树维护.md
# 对线段内的点都有直线差值修改，使用差分线段树标记




import init_setting
from cflibs import *
from lib.fenwicktree import FenwickTree
def main():
    n, q = MII()
    
    fen_x_k = FenwickTree(n + 2)
    fen_x_b = FenwickTree(n + 2)
    
    fen_y_k = FenwickTree(n + 2)
    fen_y_b = FenwickTree(n + 2)
    
    fen_x_k.add(0, 1)
    
    outs = []
    
    for _ in range(q):
        query = LII()
        
        if query[0] == 1:
            l = query[1]
            r = query[2]
            
            if l == r: continue
            
            x1 = fen_x_k.rsum(0, l) * l + fen_x_b.rsum(0, l)
            x2 = fen_x_k.rsum(0, r) * r + fen_x_b.rsum(0, r)
            
            if x1 == x2:
                fen_x_k.add(l, 1)
                fen_x_k.add(r + 1, -1)
                
                fen_x_b.add(l, -l)
                fen_x_b.add(r + 1, l)
                
                fen_y_k.add(l, -1)
                fen_y_k.add(r + 1, 1)
                
                fen_y_b.add(l, l)
                fen_y_b.add(r + 1, -l)
            else:
                fen_x_k.add(l, -1)
                fen_x_k.add(r + 1, 1)
                
                fen_x_b.add(l, l)
                fen_x_b.add(r + 1, -l)
                
                fen_y_k.add(l, 1)
                fen_y_k.add(r + 1, -1)
                
                fen_y_b.add(l, -l)
                fen_y_b.add(r + 1, l)
            
        else:
            j = query[1]
            
            x = fen_x_k.rsum(0, j) * j + fen_x_b.rsum(0, j)
            y = fen_y_k.rsum(0, j) * j + fen_y_b.rsum(0, j)
    
            outs.append(f'{x} {y}')
    
    print('\n'.join(outs))

main()
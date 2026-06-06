# https://codeforces.com/gym/104782/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0530/solution/cf104782d.md
# algorithm/codeforce/docs/线段树DP.md
# algorithm/codeforce/docs/线段树DP2.md
# #线段树DP，DP加速
# 分析运动规律，一定有一个最后的点V，从这个点开始，A，B都会全速运行，如果B被Block了，这个点就不是最后点V
#       如果没有点V，一开始就是全速运行，这时候l就是点V，
#       这时从右到左看，就会发现全速运行的条件是 ya + xb 一直增大，或者 yb是最大值的时候前一个点就是V 
#       如果V在左节点 就是ya + xb  如果 V在右节点，就是yb,直接取最大值就好了


import init_setting
from lib.cflibs import *
from lib.segTreeWithFindFirst import *
def main():
    n = II()
    v1 = LII()
    v2 = LII()
    
    vals = [(v2[i] - v1[i], v2[i]) for i in range(n)]
    
    def f(a, b):
        xa, ya = a
        xb, yb = b
        
        x = xa + xb
        y = fmax(ya + xb, yb)
        
        return (x, y)
    
    inf = 10 ** 15
    seg = SegTree(f, (0, -inf), arr= vals)
    
    q = II()
    outs = []
    
    for _ in range(q):
        l, r = GMI()
        outs.append(seg.prod(l, r + 1)[1])
    
    print('\n'.join(map(str, outs)))

main()
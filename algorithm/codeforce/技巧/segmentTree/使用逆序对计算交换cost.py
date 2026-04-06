# https://codeforces.com/gym/102911/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0404/solution/cf102911h.md


import init_setting
from cflibs import *
from lib.fenwicktree import FenwickTree
def main(): 
    n = II()
    v1 = LII()
    v2 = LII()
    
    st_range = sorted(range(n), key=lambda x: v1[x])
    
    fen = FenwickTree(n)
    
    ans = 0
    for i in st_range:
        ans += fen.rsum(i, n - 1) * v2[i]
        fen.add(i, v2[i])
    
    print(ans)

main()
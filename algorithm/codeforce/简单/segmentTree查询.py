# https://codeforces.com/gym/105709/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0411/solution/cf105709f.md
# 使用segmentTree查询区间和，
# 


import init_setting
from lib.cflibs import *
from lib.fenwicktree import *
def main(): 
    n, k = MII()
    bs = LII()
    ws = LII()
    vs = LII()
    
    tmp = [[] for _ in range(k)]
    
    for i in range(n):
        if bs[i] + ws[i] <= k:
            tmp[bs[i]].append(i)
    
    fen = FenwickTree(k)
    ans = 0
    
    for i in range(1, k):
        for idx in tmp[i]:
            fen.add(ws[idx], vs[idx])
        ans = fmax(ans, fen.rsum(0, k - i))
    
    print(ans)

main()
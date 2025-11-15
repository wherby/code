# https://codeforces.com/gym/106185/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1113/solution/cf106185i.md
#首先，考虑每个数字只有两个位置的情况。此时考虑用线把相等数字两两连起来。
#我们最终状态需要所有线之间两两有交点。而每次交换相邻两个人的位置只能新增一个交点，所以答案是 comb(n,2) - 交点数
# 需要计算有重复数字的时候的最多的交点数目， 则把重复数字按照前后一一匹配
# 再 用FrenwickTree 计算线段的交点数目


import init_setting
from cflibs import *
from lib.fenwicktree import *
def main(): 
    outs = []
    
    while True:
        n = II()
        if n == 0:
            break
        nums = LII()
        
        pos = [[] for _ in range(n + 1)]
        
        for i in range(2 * n):
            pos[nums[i]].append(i)
        
        to_pos = [-1] * (2 * n)
        
        for i in range(n + 1):
            k = len(pos[i]) // 2
            for j in range(k):
                to_pos[pos[i][j]] = pos[i][j + k]
        
        fen = FenwickTree(2 * n)
        
        ans = n * (n - 1) // 2
        
        for i in range(2 * n):
            if to_pos[i] >= 0:
                ans -= fen.rsum(i, to_pos[i])
                fen.add(to_pos[i], 1)
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))

main()
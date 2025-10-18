# https://codeforces.com/gym/105167/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1002/solution/cf105167j.md
# 够着相邻绝对值差最大的数列
# 利用顺序排列各自分离集合出现的元素到对应位置，然后用区间查询得到逆序对数目
# 用FenwickTree 计算逆序对的数量

import init_setting
from lib.cflibs import *
from lib.fenwicktreeOneBased import FenwickTree
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        ans = n * n
        tmp = [0] * n
        
        pt1 = 2
        pt2 = 1
        
        for i in range(n):
            if nums[i] == n // 2: tmp[i] = 0
            elif nums[i] == n // 2 + 1: tmp[i] = n - 1
            elif nums[i] < n // 2:
                tmp[i] = pt1
                pt1 += 2
            else:
                tmp[i] = pt2
                pt2 += 2
        
        fen = FenwickTree(n)
        
        total = 0
        for i in range(n - 1, -1, -1):
            total += fen.rsum(0, tmp[i])
            fen.add(tmp[i], 1)
        ans = fmin(ans, total)
        
        pt1 = 1
        pt2 = 2
        
        for i in range(n):
            if nums[i] == n // 2: tmp[i] = n - 1
            elif nums[i] == n // 2 + 1: tmp[i] = 0
            elif nums[i] < n // 2:
                tmp[i] = pt1
                pt1 += 2
            else:
                tmp[i] = pt2
                pt2 += 2
        
        fen.init()
        
        total = 0
        for i in range(n - 1, -1, -1):
            total += fen.rsum(0, tmp[i])
            fen.add(tmp[i], 1)
        ans = fmin(ans, total)
        
        outs.append(f'{n * n // 2 - 1} {ans}')
    
    print('\n'.join(outs))
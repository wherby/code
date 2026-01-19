# https://codeforces.com/gym/103483/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0119/solution/cf103483d.md
# 问题中的判定问题，A中 所有i 的所有需求能在 B中[i-mid, i-mid] 位置安排好
# 前缀和是反映统计量。 从左到右开始
# A0 对应 B[0-mid-1], A1 对应 B[0,mid].. A[i] 对应 B[i-mid+1, i+mid-1]
# 这就是 霍尔定理 相关， 
# algorithm/mathA/霍尔婚配定理/不等式变形.md
# 根据不等式变形。把不等式分裂为两个部分。当前值 cur = acc2[fmin(i + mid + 1, n)] - acc1[i + 1]
#                                  和累积值 diff = fmin(acc1[i] - acc2[fmax(i - mid, 0)], diff)
# 这两部分对应了 A[i,j]的选择 使得对于任意 i,j 都能成立




import init_setting
from cflibs import *
def main(): 
    n = II()
    v1 = LII()
    v2 = LII()
    
    acc1 = list(accumulate(v1, initial=0))
    acc2 = list(accumulate(v2, initial=0))
    
    l, r = 0, n
    while l <= r:
        mid = (l + r) // 2
        
        flg = True
        diff = 0
        for i in range(n):
            diff = fmin(acc1[i] - acc2[fmax(i - mid, 0)], diff)
            cur = acc2[fmin(i + mid + 1, n)] - acc1[i + 1]
            if cur + diff < 0:
                flg = False
        
        if flg: r = mid - 1
        else: l = mid + 1
    
    print(l if l < n else -1)
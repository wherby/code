# https://codeforces.com/gym/106443/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0401/solution/cf106443m.md
# 环形差分，用加倍的方式模拟环形,因为影响区间是m长度，所以把2m长度的值域映射到m长度上就可以了，这样差分标记虽然不对其，也可以确保在m值域上都有标记
# 因为损失函数是一个折线，所以计算折线的起始点，用 kx+b的方式做差分标记
# 因为第一段的时候是0所以b是-x ,而第2段的时候结束是0，所以b是 x+m, 
# algorithm/codeforce/docs/环形奇偶性分段函数.md 奇偶性通过  v和 m 使得分段函数统一， 如果是只有一个顶点，则分在第2段


import init_setting
from cflibs import *
def main(): 
    n, m = MII()
    nums = LII()
    
    diff_k = [0] * (m * 2 + 1)
    diff_b = [0] * (m * 2 + 1)
    
    v = (m + 1) // 2
    
    for x in nums:
        diff_k[x] += 1
        diff_k[x + v] -= 1
        diff_b[x] -= x
        diff_b[x + v] += x
        
        diff_k[x + v] -= 1
        diff_k[x + m] += 1
        diff_b[x + v] += x + m
        diff_b[x + m] -= x + m
    
    for i in range(m * 2):
        diff_k[i + 1] += diff_k[i]
        diff_b[i + 1] += diff_b[i]
    
    ans = [0] * m
    
    for i in range(m * 2):
        ans[i % m] += diff_k[i] * i + diff_b[i]
    
    print(min(ans))
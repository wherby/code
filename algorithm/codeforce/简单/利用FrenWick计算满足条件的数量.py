# https://codeforces.com/gym/106191/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1117/solution/cf106191f.md
# 利用Frenwick 计算满足条件的区域查询
# 利用同一前缀和的值排序确定Tree的大小，其实可以用sortedlist 更快求解

import init_setting
from lib.cflibs import *

def main(): 
    n = II()
    nums = LII()
    
    d = defaultdict(list)
    orig = random.getrandbits(30)
    
    cur = orig
    neg = 0
    
    d[cur].append(0)
    
    for i in range(n):
        cur += nums[i]
        if nums[i] < 0: neg += 1
        else: neg -= 1
        d[cur].append(neg)
    
    for x in d.values():
        x.sort()
    
    fens = {x: FenwickTree(len(d[x])) for x in d}
    
    ans = 0
    
    cur = orig
    neg = 0
    
    fens[cur].add(bisect.bisect_left(d[cur], neg), 1)
    
    for i in range(n):
        cur += nums[i]
        if nums[i] < 0: neg += 1
        else: neg -= 1
        
        p = bisect.bisect_left(d[cur], neg)
        ans += fens[cur].rsum(0, p)
        fens[cur].add(p, 1)
    
    print(ans)
# https://codeforces.com/gym/106107/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1122/solution/cf106107b.md
# 固定r,选择l,对于当前r而言，需要a[r] 没在b[l~r]中，所以需要l从a[r]在b中出现过的最后一次位置开始查询
#            对于l的选择而言，需要a[l]在b[l~r]中出现，所以当a[r]出现了，则b中所有等于a[r]值的 l 都能满足条件,但是a[r]出现的位置会出现很多次，所以需要把 index 数组在出现的时候清零并设置

import init_setting
from cflibs import *
from lib.fenwicktree import *
def main(): 
    t = II()
    outs = []
    rnd = random.getrandbits(30)
    
    for _ in range(t):
        n = II()
        v1 = [x ^ rnd for x in MII()]
        v2 = [x ^ rnd for x in MII()]
        
        ans = 0
        
        fen = FenwickTree(n)
        
        cur_status = defaultdict(list)
        last_pos = {}
        
        for i in range(n):
            last_pos[v2[i]] = i
            start = last_pos[v1[i]] + 1 if v1[i] in last_pos else 0
            
            cur_status[v1[i]].append(i)
            while cur_status[v2[i]]:
                fen.add(cur_status[v2[i]].pop(), 1)
            
            ans += fen.rsum(start, i)
    
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))
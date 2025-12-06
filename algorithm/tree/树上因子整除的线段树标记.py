
# https://codeforces.com/gym/105056/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1203/solution/cf105056f.md
# 使用SegmentTree 在树上做最小前缀和操作
# 对于整除的计算 lambda x, y: x * y % k  作为合并算法
# 这样可以使得不用计算因数因子。
# 而在树上使用 ~u作为出栈标记，在出栈时候把位子上的因子置为1


import init_setting
from cflibs import *
from lib.segTreeWithFindFirst import SegmentTree
def main(): 
    n, k, q = MII()
    nums = LII()
    parent = LII()
    
    path = [[] for _ in range(n)]
    for i in range(n - 1):
        path[parent[i] - 1].append(i + 1)
    
    updates = [[] for _ in range(n)]
    
    for qid in range(q):
        u, x = MII()
        u -= 1
        updates[u].append((qid+1, x))   #注意index 偏移  可能是 SegmentTree 实现不同，或者 max_right 的定义不一致，这里需要对 qid +1 
    
    seg = SegmentTree(lambda x, y: x * y % k, 1, [1]*(q+1))
    ans = [0] * n
    
    stk = [0]
    #print(updates)
    
    while stk:
        u = stk.pop()
        
        if u >= 0:
            for qid, x in updates[u]:
                seg.set(qid, x)
            
            if nums[u] % k == 0: ans[u] = 0
            else:
                res = seg.max_right(0, lambda x: x * nums[u] % k)
                ans[u] = -1 if res == q else res + 1
            
            stk.append(~u)
            for v in path[u]:
                stk.append(v)
            
        else:
            for qid, x in updates[~u]:
                seg.set(qid, 1)
    
    print(' '.join(map(str, ans)))

main()
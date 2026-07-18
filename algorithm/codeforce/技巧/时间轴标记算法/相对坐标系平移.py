# https://codeforces.com/gym/103306/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0714/solution/cf103306h.md
# 使用相对坐标系平移和维护原始坐标相对位置，维护二维偏序排列，使用线段树功能维护状态和查询
# 使用时间轴标记的方式维护了系统任意时刻的状态


import init_setting
from cflibs import *
from lib.segTreeWithFindFirst import SegTree
def main():
    n, m = MII()
    p = LII()
    ts = LII()
    
    M = 2 * 10 ** 5 + 5
    
    updates = [set() for _ in range(M)]
    next_update = [0] * n
    
    rnd = random.getrandbits(30)
    
    cur_status = [0] * n
    
    for i in range(n):
        cur = i % (2 * p[i])
        
        if cur < p[i]:
            cur_status[i] = 1
            next_update[i] = p[i] - cur
            updates[p[i] - cur].add(i ^ rnd)
        
        else:
            cur_status[i] = 0
            next_update[i] = 2 * p[i] - cur
            updates[2 * p[i] - cur].add(i ^ rnd)
    
    seg = SegTree(fmax, 0,arr= cur_status)
    
    ans = [0] * m
    
    st_range = sorted(range(m), key=lambda x: ts[x])
    pt = 0
    
    for i in range(10 ** 5 + 5):
        for msk in updates[i]:
            idx = msk ^ rnd
            seg.set(idx, seg.get(idx) ^ 1)
    
            next_update[idx] = i + p[idx]
            updates[i + p[idx]].add(idx ^ rnd)
        
        updates[i].clear()
        
        if pt < m and ts[st_range[pt]] == i:
            if seg.all_prod() == 0: ans[st_range[pt]] = -1
            else:
                idx = seg.max_right(0, lambda x: x == 0)
                idx +=1 #
                ans[st_range[pt]] = idx
                
                seg.set(idx, seg.get(idx) ^ 1)

                updates[next_update[idx]].remove(idx ^ rnd)
                next_update[idx] = i + p[idx] + 1
                updates[i + p[idx] + 1].add(idx ^ rnd)
            pt += 1
    
    print('\n'.join(f'{ans[i]} {ts[i] + ans[i]}' if ans[i] >= 0 else '-1 -1' for i in range(m)))

main()
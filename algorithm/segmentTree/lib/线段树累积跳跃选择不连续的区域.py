# https://codeforces.com/gym/106164/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0513/solution/cf106164f.md
# 这里按照H从大到小依次激活各个点
# 需要使得从前到后访问对的节点Pi的总和小于 P, 
# 这里 并不能保证是某个index前面连续都能选中，
# 比如 P= 10 ， 激活的 PList =[6,5,4]  这时候只能选中[6,4] 两个节点
# 所以需要用线段树的 max_right 找到可以连续选中的最大区块，然后更新剩余值，再继续，因为每次选中的时候，必然会让P的剩余规模减半，所以这个跳跃最多有LogP 次，实际上会更快




import init_setting
from cflibs import *
from lib.segTreeWithFindFirst2 import SegTree
def main(): 
    bound = 10 ** 18 + 5
    def add(x, y):
        return fmin(x + y, bound)
    
    t = II()
    outs = []
    
    for _ in range(t):
        n, p = MII()
        
        hs = []
        ps = []
        
        for _ in range(n):
            h_val, p_val = MII()
            hs.append(h_val)
            ps.append(p_val)
        
        order = sorted(range(n), key=lambda x: -hs[x])
        
        seg = SegTree(add, 0, n)
        seg_happiness = SegTree(add, 0, n)
        
        ans = -1
        chosen_threshold = -1
        
        for i in range(n):
            seg.set(order[i], ps[order[i]])
            seg_happiness.set(order[i], hs[order[i]])
            
            if i == n - 1 or hs[order[i]] != hs[order[i + 1]]:
                cur_pos = 0
                cur_p = p
                
                res = 0
                
                while True:
                    l, r = cur_pos, n - 1
                    while l <= r:
                        mid = (l + r) // 2
                        if ps[mid] > cur_p: l = mid + 1
                        else: r = mid - 1
                    
                    cur_pos = l
                    if cur_pos == n: break
                    
                    n_cur_pos = seg.max_right(cur_pos, lambda x: x <= cur_p)
                    cur_p -= seg.prod(cur_pos, n_cur_pos)
                    res += seg_happiness.prod(cur_pos, n_cur_pos)
                    
                    cur_pos = n_cur_pos
                
                if res >= ans:
                    ans = res
                    chosen_threshold = hs[order[i + 1]] if i != n - 1 else 0
        
        outs.append(f'{ans} {chosen_threshold}')
    
    print('\n'.join(outs))

main()
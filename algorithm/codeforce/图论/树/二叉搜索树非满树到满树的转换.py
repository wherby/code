# https://codeforces.com/gym/103503/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0311/solution/cf103503b.md
# 题目是求一个可能不满树的二叉数的idx在当前搜索算法下的输出数字编号.
# 而满树的情况，二叉搜索就是如果当前节点是idx,则此时可以用cur记录得到当前的序号
# 如果最下层不满了，则搜索到最后一层的时候，ans = -1 ,这时就需要用到 idx 表示此节点为满树的情况下的编号，加上上一层所有的节点 cnt//2 ，而last_cnt 则记录的是上一层所有的节点中 < idx 的节点数量。
# 因为是搜索树的情况下，最后一层的序号 == idx - （上一层 < idx 的节点数量） 
# 然后最后一层的数字编号则等于 最后一层的序号 + 上一层的节点数量

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, idx = MII()
        ans = -1
        
        l, r = 1, n
        cur = 1
        last_cnt = 0
        cnt = 1
        
        while cnt <= n:
            mid = (l + r) // 2
            
            if idx >= mid: last_cnt = last_cnt * 2 + 1
            else: last_cnt = last_cnt * 2
            
            if idx == mid:
                ans = cur
                break
            
            if idx < mid:
                r = mid - 1
                cur = cur * 2
            else:
                l = mid + 1
                cur = cur * 2 + 1
            
            cnt = cnt * 2 + 1
        
        if ans == -1:
            ans = idx + cnt // 2 - last_cnt
        
        outs.append(ans)
    
    print(' '.join(map(str, outs)))
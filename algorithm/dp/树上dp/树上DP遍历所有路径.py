# https://codeforces.com/gym/105706/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0616/solution/cf105706b.md
# algorithm/codeforce/docs/遍历所有树上路径.md
# 需要遍历树上所有路径的，遍历的方式就是遍历所有节点为端点的，向上，向下的所有路径
# 对于向下路径很简单，用逆DFS序就能得到， 对于向上的路径，需要维护rev_dp记录，而向上有两种情况，从父亲哪里直接向上则用rev_dp 递推， 从 父亲那里向下，则是有N种可能
# 如果每个点都遍历就变成了N**2，所以这里用了前后缀对齐的方式，在对齐的前后缀的时候，正好少了自己，就符合从该点到所有可能的兄弟节点的路径了
# 这里因为是要满足 k<=y<=k**2, 所以对于区间压缩就是，如果两个点的距离小于2倍，则认为他们是“相邻的”，这样就可以合并区间了



import init_setting
from lib.cflibs import *
def main():
    def simplify(tmp):
        ans = []
        
        for l, r in tmp:
            if len(ans) == 0:
                ans.append((l, r))
            else:
                if ans[-1][1] * 2 >= l:
                    vl, vr = ans.pop()
                    ans.append((fmin(l, vl), fmax(r, vr)))
                else:
                    ans.append((l, r))
        
        return ans
    
    def merge(intervals1, intervals2):
        tmp = []
        p1, p2 = 0, 0
        
        while p1 < len(intervals1) and p2 < len(intervals2):
            if intervals1[p1] < intervals2[p2]:
                tmp.append(intervals1[p1])
                p1 += 1
            else:
                tmp.append(intervals2[p2])
                p2 += 1
        
        while p1 < len(intervals1):
            tmp.append(intervals1[p1])
            p1 += 1
        
        while p2 < len(intervals2):
            tmp.append(intervals2[p2])
            p2 += 1
        
        return simplify(tmp)
    
    t = II()
    outs = []
    
    for _ in range(t):
        n, q = MII()
        path = [[] for _ in range(n)]
        
        for _ in range(n - 1):
            u, v, w = MII()
            u -= 1
            v -= 1
            path[u].append(w * n + v)
            path[v].append(w * n + u)
        
        parent = [-1] * n
        que = [0]
        
        for u in que:
            for msk in path[u]:
                v = msk % n
                if parent[u] != v:
                    parent[v] = u
                    que.append(v)
        
        dp = [[(0, 0)] for _ in range(n)]
        
        for u in reversed(que):
            for msk in path[u]:
                w, v = divmod(msk, n)
                if parent[v] == u:
                    dp[u] = merge(dp[u], [(l + w, r + w) for l, r in dp[v]])
        
        rev_dp = [[] for _ in range(n)]
        
        for u in que:
            pre = [[]]
            for msk in path[u]:
                w, v = divmod(msk, n)
                if parent[v] == u:
                    pre.append(merge(pre[-1], [(l + w, r + w) for l, r in dp[v]]))
            
            suf = [[]]
            for msk in reversed(path[u]):
                w, v = divmod(msk, n)
                if parent[v] == u:
                    suf.append(merge(suf[-1], [(l + w, r + w) for l, r in dp[v]]))
            
            pre.reverse()
            suf.pop()
            
            for msk in path[u]:
                w, v = divmod(msk, n)
                if parent[v] == u:
                    rev_dp[v] = merge([(l + w, r + w) for l, r in rev_dp[u]], [(l + w, r + w) for l, r in merge(suf.pop(), pre.pop())])
        
        total_merge = []
        while dp: total_merge = merge(total_merge, dp.pop())
        while rev_dp: total_merge = merge(total_merge, rev_dp.pop())
        
        ans = []
        
        for _ in range(q):
            val = II()
            flg = False
            
            for l, r in total_merge:
                if (l + 1) // 2 <= val <= r:
                    flg = True
            
            ans.append(1 if flg else 0)
        
        outs.append(''.join(map(str, ans)))
    
    print('\n'.join(outs))
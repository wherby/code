# https://codeforces.com/gym/106732/problem/F2
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1003/solution/cf106732f2.md
# 这里首先是对子树的贪心计算，
#    对于赚钱的子树: 排序依据： 应该按起步门槛（v0[i]）从小到大（升序） 排在最前面
#    对于亏钱的子树: 排序依据： 应该按ws[i] - v0[i] 升序（相当于按“末尾剩余电量要求”降序）排在后面。
# 然后对于留下哪个子树作为完成子树，则需要遍历得到最小的完成起点数量
# algorithm/codeforce/dp/docs/树上DP前后缀子树处理.md
# dp0: 表示完整走完此子树需要的最少电量
# dp1：表示当前子树为最后访问子树需要的最少电量
# tot：表示访问完成子树的电量变化
# algorithm/codeforce/docs/贪心排序.md





import init_setting
from lib.cflibs import *
def main():
    n = II()
    nums = LII()
    
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
            w, v = divmod(msk, n)
            if parent[u] != v:
                parent[v] = u
                que.append(v)
    
    dp0 = [0] * n
    dp1 = [inf] * n
    tot = [0] * n
    
    for u in reversed(que):
        v0 = []
        v1 = []
        ws = []
        
        for msk in path[u]:
            w, v = divmod(msk, n)
            if parent[v] == u:
                v0.append(fmax(w + dp0[v], 2 * w + tot[v]))
                v1.append(w + dp1[v])
                ws.append(2 * w + tot[v])
                tot[u] += 2 * w + tot[v]
        
        k = len(v0)
        
        if k == 0:
            dp0[u] = 0
            dp1[u] = 0
        else:
            gain = [i for i in range(k) if ws[i] <= 0]
            cost = [i for i in range(k) if ws[i] > 0]
            gain.sort(key=lambda x: v0[x])
            cost.sort(key=lambda x: ws[x] - v0[x])
            st_range = gain + cost
            
            suff = [0] * (k + 1)
            for idx in range(k - 1, -1, -1):
                i = st_range[idx]
                suff[idx] = fmax(suff[idx + 1] + ws[i], v0[i])
            
            cur_w = 0
            for idx in range(k):
                i = st_range[idx]
                dp1[u] = fmin(dp1[u], max(dp0[u], suff[idx + 1] + cur_w, tot[u] - ws[i] + v1[i]))
                dp0[u] = fmax(dp0[u], v0[i] + cur_w)
                cur_w += ws[i]
        
        dp0[u] = fmax(dp0[u] - nums[u], 0)
        dp1[u] = fmax(dp1[u] - nums[u], 0)
        tot[u] -= nums[u]
    
    print(dp1[0])
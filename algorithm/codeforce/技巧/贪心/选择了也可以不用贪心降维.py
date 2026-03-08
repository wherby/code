# https://codeforces.com/contest/2200/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0228/solution/cf2200f.md
# 从商店买了一个粒子也可以不用，
# 所以需要从大到小维护两个值，一个是当前i 和当前值 i+1 的最大值，
# i+1作为不选商店粒子的值，i作为选商店粒子的值,
# 为了使得计算粒子的值能用hash的方式计算，则需要用贪心维护每个y的最大值，
# 因为y表示阵容大小，阵容大的时候必然能兼容小阵容的粒子组合，所以可以用贪心计算每个y可以达到的最大值
# 贪心降维，使得Y的搜索变成O(1)的字典查找



import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        
        tmp = [[] for _ in range(n + 1)]
        for _ in range(n):
            x, y = MII()
            tmp[y].append(x)
        
        ans = 0
        to_add = [0] * (n + 1)
        
        pq = []
        cur = 0
        
        for i in range(n, -1, -1):
            for x in tmp[i]:
                heappush(pq, x)
                cur += x
            while len(pq) > i + 1:
                cur -= heappop(pq)
            
            ans = fmax(ans, cur)
            to_add[i] = cur - (pq[0] if len(pq) == i + 1 else 0)
        
        for i in range(1, n + 1):
            to_add[i] = fmax(to_add[i], to_add[i - 1])
        
        res = []
        for _ in range(m):
            x, y = MII()
            res.append(fmax(ans, to_add[y] + x))
        
        outs.append(' '.join(map(str, res)))
    
    print('\n'.join(map(str, outs)))
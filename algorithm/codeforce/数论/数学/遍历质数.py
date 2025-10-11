# https://codeforces.com/gym/104328/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1009/solution/cf104328d.md
# 要求路径上公约数不为1 的路径最长路径
# 因为公约数不为1，所以质数的路径最长，遍历
# 换根DP求路径长度的一次遍历解法
# 反向遍历(dfs) dp[i]记录 最长杜绝长度，路径长度由当前节点和最长2个子路径构成



import init_setting
from cflibs import *
def main():
    M = 10 ** 7
    prime_factor = list(range(M + 1))
    
    for i in range(2, M + 1):
        if prime_factor[i] == i:
            for j in range(i, M + 1, i):
                prime_factor[j] = i
    
    n = II()
    nums = LII()
    
    path = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    cnt = [0] * (M + 1)
    
    for x in nums:
        while x > 1:
            p = prime_factor[x]
            cnt[p] += 1
            while x % p == 0:
                x //= p
    
    parent = [-1] * n
    que = [0]
    
    for u in que:
        for v in path[u]:
            if parent[u] != v:
                parent[v] = u
                que.append(v)
    
    que.reverse()
    dp = [0] * n
    
    for i in range(M + 1):
        if cnt[i] * 2 > n:
            total = 0
    
            for u in que:
                if nums[u] % i == 0: dp[u] = 1
                else: dp[u] = 0
                
                if dp[u]:
                    v1, v2 = 0, 0
                    for v in path[u]:
                        if parent[v] == u:
                            if dp[v] > v1: v1, v2 = dp[v], v1
                            elif dp[v] > v2: v2 = dp[v]
                    
                    dp[u] = v1 + 1
                    total = fmax(total, v1 + v2 + 1)
            
            if total * 2 > n:
                exit(print('YES'))
    
    print('NO')
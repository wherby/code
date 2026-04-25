# https://codeforces.com/gym/106495/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0424/solution/cf106495e.md
# 使用DFS实现


import sys

# 增加递归深度以防 N 很大
sys.setrecursionlimit(2000000)

def solve_erasmus():
    # 假设输入 N, Q 已经获取
    n, q = MII()
    
    # 1. 线性筛获取质数
    primes = []
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n: break
            is_prime[i * p] = False
            if i % p == 0: break
            
    order = []
    
    # 2. DFS 生成字典序序列
    # val: 当前累乘的数值, p_idx: 当前可以使用的质数在 primes 中的起始索引
    def dfs(val, p_idx):
        order.append(val)
        
        # 遍历可选的质数
        for i in range(p_idx, len(primes)):
            p = primes[i]
            next_val = val * p
            if next_val > n:
                break # 后面的质数更大，乘积肯定也超了
            
            # 递归：继续使用当前的质数 p 以及之后的质数
            dfs(next_val, i)

    # 从 1 开始 DFS，初始可用质数索引为 0 (即质数 2)
    dfs(1, 0)
    
    # 3. 处理查询
    results = []
    for _ in range(q):
        k = int(sys.stdin.readline())
        results.append(order[k-1])
        
    sys.stdout.write('\n'.join(map(str, results)) + '\n')
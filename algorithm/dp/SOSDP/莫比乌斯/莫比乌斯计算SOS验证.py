MOD = 10**9 + 7

def count_all_exact_or_subsets(nums, m=None):
    if not nums:
        return []
    
    if m is None:
        max_or = 0
        for x in nums:
            max_or |= x
        m = max_or.bit_length()
        if (1 << m) <= max_or:
            m += 1
    
    M = 1 << m
    
    # 步骤 1: 频率数组
    f = [0] * M
    for x in nums:
        if x < M:
            f[x] += 1
    
    # 步骤 2: 计算每个 mask 对应的单元素子集数
    g = [0] * M
    for mask in range(M):
        if f[mask] > 0:
            g[mask] = (pow(2, f[mask], MOD) - 1) % MOD
    
    # 步骤 3: OR-SOS DP
    # dp[mask] = OR 值恰好等于 mask 的子集数
    dp = [0] * M
    dp[0] = 1  # 空集
    
    # 对每个可能的元素值
    for x in range(M):
        if g[x] == 0:
            continue
            
        # 我们需要逆序遍历，避免重复计数
        for mask in range(M-1, -1, -1):
            if dp[mask] > 0:
                new_mask = mask | x
                dp[new_mask] = (dp[new_mask] + dp[mask] * g[x]) % MOD
    
    # 步骤 4: 减去空集
    dp[0] = (dp[0] - 1) % MOD
    if dp[0] < 0:
        dp[0] += MOD
    
    return dp

# 测试
nums = [1, 2, 3,4,5]
results = count_all_exact_or_subsets(nums)
for target in range(len(results)):
    if results[target] > 0:
        print(f"OR = {target}: {results[target]} 个子集")
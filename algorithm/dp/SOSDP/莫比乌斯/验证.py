
MOD = 10**9 + 7

def count_all_exact_or_subsets_brute(nums, m=None):
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
    
    # 暴力枚举所有子集验证
    from collections import defaultdict
    count = defaultdict(int)
    
    n = len(nums)
    for mask in range(1, 1 << n):  # 跳过空集
        val = 0
        for i in range(n):
            if mask >> i & 1:
                val |= nums[i]
        if val < M:
            count[val] += 1
    
    result = [0] * M
    for k, v in count.items():
        result[k] = v % MOD
    
    return result

# 用暴力法验证
nums = [1, 2, 3,4,5]
results = count_all_exact_or_subsets_brute(nums)
for target in range(len(results)):
    if results[target] > 0:
        print(f"OR = {target}: {results[target]} 个子集")
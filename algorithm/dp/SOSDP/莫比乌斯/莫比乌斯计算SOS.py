from typing import List, Dict

# 定义模数
MOD = 1_000_000_007

def count_subsequence_or_values(nums: List[int]) -> Dict[int, int]:
    """
    计算数组中所有子序列的按位或结果恰好等于 K 的数量。
    使用 SOS DP 和集合反演实现。

    Args:
        nums: 输入的整数数组。

    Returns:
        一个字典，键 K 为按位或的值，值为恰好等于 K 的子序列数量 (取模)。
    """
    if not nums:
        return {0: 0} # 空数组只有一个空子序列，OR 为 0，数量为 1 (如果允许空子序列)

    N = len(nums)
    
    # 确定最大需要的位数 M
    max_val = 0
    if nums:
        max_val = max(nums)
    
    # 确定最大的位 M (例如，10^9 约需 30 位)
    # bit_length() 返回表示该整数所需的最小位数
    max_bit = max_val.bit_length()
    
    # 状态空间大小 U = 2^M
    U = 1 << max_bit
    
    # --- 步骤 1 & 2: SOS DP 预处理 ---
    
    # f[x]: 元素 x 在 nums 中出现的次数
    f = [0] * U
    for x in nums:
        # 确保 x 在 U 范围内，避免越界
        if x < U:
            f[x] += 1
            
    # 执行 SOS DP：f[V] 存储所有是 V 的子集的元素的总个数
    for i in range(max_bit):
        mask = 1 << i
        for v in range(U):
            if (v & mask):
                # f[v] 包含 f[v 移除第 i 位]
                # 相当于 f[v] += f[v - mask]
                f[v] = (f[v] + f[v ^ mask]) 
    
    # --- 步骤 3: 计算 G(V) ---
    
    # G[V] = 2^f[V]：按位或值是 V 的子集的子序列数量
    # pow2 数组用于加速计算
    pow2 = [1] * (N + 1)
    for i in range(1, N + 1):
        pow2[i] = (pow2[i - 1] * 2) % MOD

    # G 数组
    G = [0] * U
    for v in range(U):
        # 确保 f[v] <= N
        count = min(f[v], N) 
        G[v] = pow2[count]
        
    # --- 步骤 4: 逆向 SOS DP (集合反演), 得到 F(K) ---
    
    # F[K] 存储 OR 结果恰好是 K 的子序列数量
    F = G[:] 
    
    for i in range(max_bit):
        mask = 1 << i
        for v in range(U):
            if (v & mask):
                # F[V] = F[V] - F[V 移除 i 位] (莫比乌斯反演公式)
                # 逆向 SOS DP: F[v] -= F[v ^ mask]
                F[v] = (F[v] - F[v ^ mask] + MOD) % MOD
                
    # --- 5. 格式化结果 ---
    
    results: Dict[int, int] = {}
    for k in range(U):
        if F[k] > 0:
            # F[0] 包含了空子序列 (OR=0，数量为 1)。如果要求非空子序列，需要特殊处理。
            if k == 0:
                # F[0] = (所有 OR 是 0 的子序列数量)
                # 非空子序列数量 = F[0] - 1
                non_empty_count = (F[k] - 1 + MOD) % MOD
                if non_empty_count > 0:
                    results[k] = non_empty_count
            else:
                results[k] = F[k]
                
    return results

# 示例调用
nums1 = [1, 2, 3,4,5] # 二进制: [01, 10, 11]
# 期望结果: OR=1, 2, 3
# OR=1: [1]
# OR=2: [2]
# OR=3: [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
result1 = count_subsequence_or_values(nums1)

print(f"输入数组: {nums1}")
print("按位或结果的子序列数量 (非空):")
for k, count in sorted(result1.items()):
    print(f"  OR = {k}: {count}")

# print("-" * 20)

# nums2 = [4, 6, 7] # 二进制: [100, 110, 111]
# result2 = count_subsequence_or_values(nums2)
# print(f"输入数组: {nums2}")
# print("按位或结果的子序列数量 (非空):")
# for k, count in sorted(result2.items()):
#     print(f"  OR = {k}: {count}")
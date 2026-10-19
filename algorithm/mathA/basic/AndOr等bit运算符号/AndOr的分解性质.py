# https://leetcode.cn/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/?envType=daily-question&envId=2026-10-12
# 给你一个下标从 0 开始的整数数组 nums 和一个 正 整数 k 。
# 你可以对数组执行以下操作 任意次 ：
# 选择两个互不相同的下标 i 和 j ，同时 将 nums[i] 更新为 (nums[i] AND nums[j]) 且将 nums[j] 更新为 (nums[i] OR nums[j]) ，OR 表示按位 或 运算，AND 表示按位 与 运算。
# 你需要从最终的数组里选择 k 个元素，并计算它们的 平方 之和。
# 请你返回你可以得到的 最大 平方和。
# 由于答案可能会很大，将答案对 109 + 7 取余 后返回。



class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        dp=[0]*32
        for a in nums:
            for i in range(32):
                if a &(1<<i):
                    dp[i] +=1
        acc = 0 
        for _ in range(k):
            cur = 0
            for i in range(32):
                if dp[i]:
                    cur += 1<<i
                    dp[i] -=1
            acc += cur **2
            acc %= mod 
        return acc
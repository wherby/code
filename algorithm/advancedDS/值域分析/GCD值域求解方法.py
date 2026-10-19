# https://leetcode.cn/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-ii/description/
# 给你一个整数数组 nums 和一个整数 k。
# 如果一个子数组的和能够被 k 整除，或者在 将该子数组中的一个元素取反 后能使和被 k 整除，则称该子数组是 有效的 。
# 将一个元素取反意味着将其值 x 替换为 -x。
# 返回 最长有效子数组的长度 。如果不存在有效的子数组，则返回 0。
# 子数组 是数组中一个连续且非空的元素序列。
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= k <= 3000

# 题目中由于k相对较小，所以在值域范围内求解
# 使用 gcd性质优化更简单： algorithm/array/subArray/值域求解gcd优化.py
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n= len(nums)
        lst =[-1]*k 
        fst = [-2]*k 
        lls = [[] for _ in range(k)]
        cur = [0]*k
        acc = 0
        for i,a in enumerate(nums):
            a = a % k 
            acc = (acc+a)%k 
            lst[acc] = i 
            lls[a].append(i)
        acc = 0
        ans = 0
        for i,a in enumerate(nums):
            a = a %k
            if fst[acc] ==-2:
                fst[acc] = i-1
                ans = max(ans, lst[acc] - i+1 )
                for j,b in enumerate(lst):
                    if b>=i and b-i+1 > ans:
                        for i1 in range(3):
                            d = i1*k +j
                            if d >=acc and  (d-acc)%2 ==0  and (d-acc)//2 <k :
                                c = (d-acc)//2
                                while cur[c] < len(lls[c]) and lls[c][cur[c]]< i:
                                    cur[c] +=1
                                if cur[c] < len(lls[c]) and lls[c][cur[c]]<=b:
                                    ans = max(ans,b-i+1)
            
            acc =(acc+a)%k 
        return ans
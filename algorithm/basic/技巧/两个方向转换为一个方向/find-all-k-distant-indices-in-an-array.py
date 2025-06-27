# https://leetcode.cn/problems/find-all-k-distant-indices-in-an-array/description/?envType=daily-question&envId=2025-06-24
from typing import List, Tuple, Optional
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ret= []
        lst = -k-1 
        for i in range(k):
            if nums[i] == key:
                lst = i 
        n = len(nums)
        for i in range(n):
            if i + k < n and nums[i+k] == key:
                lst = i+k 
            if lst >= i-k:
                ret.append(i)
        return ret 
        

nums = [734,228,636,204,552,732,686,461,973,874,90,537,939,986,855,387,344,939,552,389,116,93,545,805,572,306,157,899,276,479,337,219,936,416,457,612,795,221,51,363,667,112,686,21,416,264,942,2,127,47,151,277,603,842,586,630,508,147,866,434,973,216,656,413,504,360,990,228,22,368,660,945,99,685,28,725,673,545,918,733,158,254,207,742,705,432,771,578,549,228,766,998,782,757,561,444,426,625,706,946]

re = Solution().findKDistantIndices(nums,939,34)
print(re)
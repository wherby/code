from bisect import bisect_left
class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(1001):
            k = bisect_left(nums,i)
            if i == n-k:
                return i
        return -1

re =Solution().specialArray(nums = [0,0])
print(re)


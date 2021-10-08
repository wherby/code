class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    cnt +=1
        return cnt

re= Solution().numOfPairs(["1","1","1"],"11")
print(re)
import math
class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        sm = sum(nums)
        diff = abs(goal - sm)
        return math.ceil(diff/limit)

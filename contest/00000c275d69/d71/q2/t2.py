class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        a1 = list(filter(lambda x: x < pivot, nums))
        a2 =list(filter(lambda x : x>pivot,nums))
        a3 = list(filter(lambda x : x == pivot,nums))
        return a1 +a3+a2

re =Solution().pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10)
print(re)
class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        st= []
        n = len(nums)
        for i,a in enumerate(nums):
            while len(st)>0 and st[-1] >a and len(st) + n-i  >k:
                st.pop()
            st.append(a)
        return st[:k]

re = Solution().mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4)
print(re)

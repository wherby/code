class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(queries)
        re = [0]*n 
        for j,(k,l) in enumerate(queries):
            st =[]
            for i,num in enumerate(nums):
                st.append((int(num[-l:]),i))
            st.sort()
            re[j] = st[k-1][1]
        return re





re =Solution().smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]])
print(re)
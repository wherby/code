from sortedcontainers import SortedList
class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        st=SortedList()
        mx = 0
        for a in nums:
            ridx = st.bisect_left((a,0))
            lidx  = st.bisect_left((a-k,0))
            tp =0
            for idx in range(lidx,ridx):
                tp = max(tp, st[idx][1])
            st.add((a,tp+1))
            mx =max(mx,tp+1)
        return mx
re =Solution().lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3)
print(re)
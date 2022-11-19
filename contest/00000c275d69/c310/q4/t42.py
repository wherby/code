# Wrong answer
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
            if ridx==lidx:
                st.add((a,1))
                mx =max(mx,1)
            else:
                idx = ridx
                while idx+1 < len(st) and st[ridx-1][1]+1  >=st[idx][1]:
                    st.discard(st[idx])  
                st.add((a, st[ridx-1][1]+1))
                mx = max(mx,st[ridx-1][1]+1)
            print(a,mx,st)
        return mx
re =Solution().lengthOfLIS(nums =[7,4,5,1,8,12,4,7], k = 5)
print(re)
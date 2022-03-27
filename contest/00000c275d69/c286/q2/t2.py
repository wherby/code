class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt= 0
        st =[]
        for a in nums:
            if len(st) %2 ==1  and a ==st[-1]:
                cnt +=1
                continue
            st.append(a)
        return cnt + len(st)%2

re =Solution().minDeletion(nums = [1,1,2,2,3,3])
print(re)
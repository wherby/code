# https://leetcode.cn/problems/ur2n8P/


from itertools import pairwise


class Solution(object):
    def sequenceReconstruction(self, nums, sequences):
        """
        :type nums: List[int]
        :type sequences: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        inOrd=[0]*n
        g =[[] for _ in range(n)]
        for sequence in sequences:
            k =len(sequence)
            for i in range(k-1):
                a =sequence[i]
                b = sequence[i+1]
                g[a-1].append(b-1)
                inOrd[b-1] +=1
        st =[]
        for i in range(n):
            if inOrd[i] ==0:
                st.append(i)
        while st:
            if len(st)>1:
                return False
            a = st.pop()
            
            for i in g[a]:
                inOrd[i] -=1
                if inOrd[i] ==0:
                    st.append(i)
        return True
        
re = Solution().sequenceReconstruction(nums = [1,2,3], sequences =[[1,2]])
print(re)
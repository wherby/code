from typing import List, Tuple, Optional
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        def getLs(ls):
            st = [(0,0)]
            ret = [0]*(n+1) 
            mx  = 0
            for i,a in enumerate(ls):
                while a < st[-1][0]:
                    st.pop()
                ret[i+1] = ret[st[-1][1]] + a * (i- st[-1][1] +1)
                st.append((a,i+1))
            return ret
        
        ls1 = getLs(maxHeights)
        ls2 = getLs(maxHeights[::-1])
        mx = 0 
        #print(ls1,ls2)
        for i in range(n):
            mx = max(mx,ls1[i] + ls2[n-i])
        return mx


re = Solution().maximumSumOfHeights([5,3,4,1,1])
print(re)
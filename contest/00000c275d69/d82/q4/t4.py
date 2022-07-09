

class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def monoStack(ls):
            ls.append(0)
            n = len(ls)
            st =[-1]
            ans =0
            for i in range(n):
                a = ls[i]
                while st and ls[st[-1]] >a:
                    k = st.pop()
                    #print(k,i,ls[k],st)
                    ans = max(ans,(i-st[-1]-1)*ls[k]) 
                    if threshold/(i-st[-1]-1) <ls[k] and ans > threshold:
                        return i-st[-1]-1
                st.append(i)
            return -1
        return monoStack(nums)



re =Solution().validSubarraySize(nums = [1,3,4,3,1], threshold = 6)
print(re)
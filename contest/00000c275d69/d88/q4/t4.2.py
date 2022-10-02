
class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)
        self.bit= [0]*self.n
        for i in range(self.n):
            self.add(i,arr[i])
    
    def sumTo(self, r):
        ret = 0
        while r >=0:
            ret += self.bit[r]
            r = (r&(r+1))-1
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx =  idx | (idx +1)

class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        ls=[]
        n = len(nums1)
        for i in range(n):
            ls.append(nums1[i]-nums2[i])
        st = FenwickTree([0]*60020)
        acc =0 
        for a in ls:
            k = 30010 + a
            acc += st.sumTo(k+diff)
            st.add(k, 1)
        return acc 

re =Solution().numberOfPairs(nums1 = [3,2,5], nums2 = [2,2,1], diff = 1)
print(re)
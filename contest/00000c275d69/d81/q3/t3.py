class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls =[0]*32
        for a in nums:
            for i in range(32):
                if a &(1<<i) != 0:
                    ls[i] =1
        ret = 0
        for i in range(32):
            if ls[i] ==1:
                ret += 1<<i
        return ret
        

re =Solution().maximumXOR([1,2,3,9,2])
print(re)
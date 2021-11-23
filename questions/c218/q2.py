# https://leetcode-cn.com/problems/max-number-of-k-sum-pairs/submissions/
from collections import defaultdict
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n= len(nums)
        dic=defaultdict(int)
        for i in nums:
            dic[i] +=1
        cnt = 0
        keys = list(dic.keys()) # if keys = dic.keys() Then there will throw exception
        #print(keys)
        for i in keys:
            a = dic[i]
            b = dic[k-i]
            if i ==k-i:
                cnt += a//2 *2
            else:
                cnt += min(a,b)
                #print(a,b,i)
        return cnt //2

re =Solution().maxOperations([3,1,3,4,3],6)
print(re)


#Traceback (most recent call last):
#  File "c:\Users\where\Documents\github\code\questions\c218\q2.py", line 25, in <module>
#    re =Solution().maxOperations([3,1,3,4,3],6)
#  File "c:\Users\where\Documents\github\code\questions\c218\q2.py", line 15, in maxOperations
#    for i in keys:
#.py
#dict_keys([3, 1, 4])
#Traceback (most recent call last):
#  File "c:\Users\where\Documents\github\code\questions\c218\q2.py", line 26, in <module>
#    re =Solution().maxOperations([3,1,3,4,3],6)
#  File "c:\Users\where\Documents\github\code\questions\c218\q2.py", line 16, in maxOperations
#    for i in keys:
#RuntimeError: dictionary changed size during iteration
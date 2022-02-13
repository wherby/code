from collections import defaultdict
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <2:
            return 0
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for i,a in enumerate(nums):
            if i %2 ==0:
                dic1[a] +=1
            else:
                dic2[a] +=1
        ls1 = []
        ls2 = []
        for key,v in dic1.items():
            ls1.append((v,key))
        for key,v in dic2.items():
            ls2.append((v,key))
        ls1= sorted(ls1,reverse= True)
        ls2 =sorted(ls2,reverse= True)
        n = len(nums)
        mx = n
        for i in range(2):
            v1,k1 =ls1[0]
            if len(ls1) >i:
                v1,k1 =ls1[i]
            for j in range(2):
                if len(ls2) > j:
                    v2,k2 = ls2[j]
                    if k1 != k2:
                        mx = min(mx, n-v1-v2)
                    else:
                        mx = min(mx,n-max(v1,v2))
        return mx

re = Solution().minimumOperations(nums = [1,2,2,2,2])
print(re)

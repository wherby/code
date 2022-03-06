class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dic ={}
        for i ,a in enumerate(mapping):
            dic[i]=a
        res = []
        for i,num in enumerate(nums):
            tp = 0
            for a in str(num):
                tp =tp*10+  dic[int(a)]
            res.append((tp +i * 0.0000001,num))
        res.sort()
        res = list(map(lambda a: a[1],res))
        return res

re = Solution().sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38])
print(re)

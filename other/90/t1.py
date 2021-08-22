class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        dic ={"##":[]}
        for k in nums:
            keys = list(dic.keys())
            for key in keys:
                kt1 = key + "#" + str(k)
                if kt1 not in dic:
                    #print(dic[key],key,dic ,kt1)
                    dic[kt1] = list(dic[key])
                    dic[kt1].append(k)
        res = list(dic.values())
        #print(res)
        return res

a =Solution().subsetsWithDup( [1,2,2])


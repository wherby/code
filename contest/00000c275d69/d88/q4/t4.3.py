from sortedcontainers import SortedDict,SortedList
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
        acc = 0
        res =SortedList()
        for a in ls :
            k = res.bisect_right(a+diff)
            acc += k
            res.add(a)
        return acc

re =Solution().numberOfPairs(nums1 = [3,2,5], nums2 = [2,2,1], diff = 1)
print(re)
from sortedcontainers import SortedDict,SortedList
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sl = SortedList()
        for a in nums1:
            sl.add(a)
        ret = []
        for a in nums2:
            idx = sl.bisect_left(a+1)
            if idx ==len(sl):
                ret.append(sl.pop(0))
            else:
                ret.append(sl.pop(idx))
        return ret

re =Solution().advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11])
print(re)
import heapq
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        st =[]
        for i,a in enumerate(nums2):
            heapq.heappush(st,(a,i))
        n = len(nums1)
        ret = [-1]*n
        notU=[]
        idx = 0
        while  idx < n:
            while idx <n and nums1[idx] <= st[0][0]:
                notU.append(nums1[idx])
                idx +=1
            if idx <n:
                a, i = heapq.heappop(st)
                ret[i] = nums1[idx]
                idx +=1
        for i,a in enumerate(ret):
            if a == -1:
                ret[i] = notU.pop()
        return ret

re =Solution().advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11])
print(re)

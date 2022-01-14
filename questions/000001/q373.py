
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(nums1)
        n = len(nums2)
        cnt =0
        st=[]
        for i in range(m):
            heapq.heappush(st, (nums1[i] + nums2[0],i,0))
        res=[]
        while st and cnt <k:
            _,i,j = heapq.heappop(st)
            if j < n-1:
                heapq.heappush(st,(nums1[i]+ nums2[j+1],i,j+1))
            res.append([nums1[i],nums2[j]])
            cnt +=1
        return res

re =Solution().kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3 )
print(re)
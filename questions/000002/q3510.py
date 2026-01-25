# https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/description/?envType=daily-question&envId=2026-01-23
# 合并的时候记录左右节点，并且保左右节点的snap 作为验证， 懒删除思路
from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0 
        n = len(nums)
        dic = {}
        st = []
        for i in range(n):
            dic[i] = (nums[i],i,i)
        for i in range(n-1):
            if nums[i]<= nums[i+1]:
                cnt +=1
            heappush(st,(nums[i] + nums[i+1],i,i+1,dic[i],dic[i+1] ))
        acc =0
        m = n
        while cnt != m-1:
            # print(st,cnt, len(nums)-1)
            # print(st)
            after,left,right,leftSnap,rightSnap = heappop(st)
            if dic[left] == leftSnap and dic[right] ==rightSnap:
                acc +=1
                if left >0:
                    if dic[left-1][0]<= dic[left][0]:
                        cnt -=1
                    if after >= dic[left-1][0]:
                        cnt +=1
                    va,l,r = dic[left-1]
                    heappush(st,(va+after,l,right,dic[left-1],(after,left,right)))
                if leftSnap[0] <= rightSnap[0]:
                    cnt -=1 
                if right < n-1:
                    if dic[right][0]<= dic[right+1][0]:
                        cnt -=1
                    if after <= dic[right+1][0]:
                        cnt +=1
                    va,l,r = dic[right+1]
                    heappush(st,(va+after,left,r,(after,left,right),dic[right+1]))
                dic[leftSnap[1]] =dic[leftSnap[2]] = dic[rightSnap[1]] = dic[rightSnap[2]] = ()
                dic[left] = (after,left,right)
                dic[right] = (after,left,right)
                m-=1
        return acc 

re = Solution().minimumPairRemoval([-2,1,2,-1,-1,-2,-2,-1,-1,1,1])
print(re)

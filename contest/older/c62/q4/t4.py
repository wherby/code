from collections import defaultdict
from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx =0
        n = len(nums)
        sm = sum(nums)
        pref = [nums[0]]*n
        dic= defaultdict(list)
        dic[nums[0]] = [0]
        for i in range(1,n-1):
            pref[i] = pref[i-1] + nums[i]
            dic[pref[i]].append(i)
        #print(dic)
        if sm %2 ==0:
            tp = sm //2
            #print(len(dic[tp]),tp)
            mx = max(mx, len(dic[tp]))
            #print(mx)
        for i in range(n):
            smt = sm + k - nums[i]
            cnt = 0
            if smt %2 ==0:
                half = smt //2
                ls1 = dic[half]
                cnt = bisect_left(ls1,i) + cnt
                ls2 = dic[half-k + nums[i]]
                cnt +=len(ls2) -  bisect_left(ls2,i)
                mx = max(mx,cnt)
        return mx

re = Solution().waysToPartition([2,-1,2],3)
print(re)
re = Solution().waysToPartition([22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14],-33)
print(re)
re = Solution().waysToPartition([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30827,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0)
print(re)

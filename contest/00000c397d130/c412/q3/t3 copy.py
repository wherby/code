from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def getFinalState(self, nums: List[int], k: int, mul: int) -> List[int]:
        mod = 10**9+7
        n = len(nums)
        kls = [0]*n
        mx = max(nums)
        if mul ==1:
            return [a%mod for a in nums]
        logls= [pow(mul,i) for i in range(40)]
        #print(logls)
        def getLog(a):
            return bisect_left(logls,a)

        for i,a in enumerate(nums):
            kls[i] = getLog(mx/nums[i])
        #print(kls)
        def verify(kk):
            acc = 0
            for a in nums:
                if a <kk:
                    acc += getLog(kk/a)
            return acc
        if sum(kls)>k:
            l,r =1,mx+1
            while l < r:
                mid = (l+r)>>1
                if verify(mid)>=k:
                    r =  mid
                else:
                    l = mid+1
            l = l-1
            for i in range(n):
                if nums[i]< l:
                    t = getLog(l/nums[i])
                    nums[i] = nums[i]*int(math.pow(mul,t))
                    k -=t
            nums = [(a,i) for i,a in enumerate(nums)]
            nums.sort()
            for i in range(k):
                nums[i]= (nums[i][0]*mul,nums[i][1])
            ret = [-1]*n 
            for i in range(n):
                a,idx = nums[i] 
                ret[idx] = a%mod
            return ret 
        else:
            #print("bn")
            k -= sum(kls)
            nums=[nums[i] * int(math.pow(mul, kls[i])) for  i in range(n)]
            nums = [(a,i) for i,a in enumerate(nums)]
           
            nums.sort()
            ret = [-1]*n
            r1 = k //n 
            res = k%n
            #print(res)
            for i in range(n):
                a,idx = nums[i]
                if i <res:
                    ret[idx] = (a * pow(mul,r1+1,mod)%mod)
                else:
                    ret[idx] = (a * pow(mul,r1,mod)%mod)
            return ret




#re =Solution().getFinalState([100000,2000], k = 2, mul = 1000000)
re =Solution().getFinalState([3,9,27,81,243,729,2187,6561,19683,59049,177147,531441,1594323,4782969,14348907,43046721,129140163,387420489], k = 1000000000, mul = 3)
#re = Solution().getFinalState([2,1,3,5,6],5,2)
#print(re)

print(pow(3,18))
print(math.log(387420489//3,3))
print(math.log(387420489/3,3.0))
print(math.log(pow(3,18),3.0)) # 18
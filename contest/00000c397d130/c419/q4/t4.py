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
from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ret = []
        n = len(nums)
        sl= SortedList([])
        for a in nums:
            sl.add((0,a))
        acc = 0
        dic ={}
        for i in range(n-k+1):

            if i ==0:
                c = Counter(nums[:k])
                for k1,v in c.items():
                    sl.add((v,k1))
                m = len(sl)
                for j in range(m-x,m):
                    acc += sl[j][0] *sl[j][1]
                    dic[tuple(sl[j])]=1
                ret.append(acc) 
            else:
                
                a = nums[i-1]
                #print(i,i-1+k)
                
                b = nums[i-1+k]
                if a !=b:
                    sl.remove((c[a],a))
                    sl.add((c[a]-1,a))
                
                    sl.remove((c[b],b))
                    sl.add((c[b]+1,b))
                    c[nums[i-1]] -=1
                    c[nums[i-1+k]]+=1
                    m = len(sl)
                    needAdd = False
                    print(dic,i,(c[a]+1,a),b)
                    del dic[(c[a]+1,a)]
                    if sl.bisect_left((c[a],a))<m-x:
                        acc -= c[a]*a
                        needAdd = True
                    else:
                        dic[(c[a],a)] =1 
                    acc -= a
                    if (c[b]-1,b) in dic:
                        acc += b
                        if needAdd:
                            x,y =sl[-x]
                            dic[(x,y)] =1   
                            acc += x*y
                    elif sl.bisect_left((c[b],b)) >=m-x:
                        if needAdd:
                            acc += c[b]*b
                            dic[(c[b],b)] =1
                        else:
                            x,y =sl[-x]
                            dic[(x,y)]  =1 
                            acc += x*y
                    else:
                        if needAdd:
                            x,y =sl[-x]
                            dic[(x,y)]  =1 
                            acc += x*y
                    #print(sl,i,a,b)
                ret.append(acc)



                
        return ret






re =Solution().findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2)
print(re)
from collections import defaultdict,deque
import functools
import heapq
import numbers
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=str(num)
        num = [int(i) for i in num]
        o,e =[],[]
        ls = [0]*len(num)
        dic={}

        for i,a in enumerate(num):
            if a %2 ==0:
                e.append((a,i))
                dic[i]=1
            else:
                o.append((a,i))
        o.sort(reverse=True)
        e.sort(reverse=True)
        oidx,eindx =0,0
        for i in range(len(num)):
            if i in dic:
                ls[i] = e[eindx][0]
                eindx +=1
            else:
                ls[i] = o[oidx][0]
                oidx +=1
        ls=[str(i) for i in ls]
        ls = "".join(ls)
        return int(ls)

re = Solution().largestInteger(1234)
print(re)

from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def splitS(s):
            ls1=""
            ls2=""
            for a in s:
                if a.isalpha():
                    ls1 +=a
                else:
                    ls2 +=a
            return [ls1,ls2]
        s1,s2 = s.split(":")
        ls1,ls2 = splitS(s1)
        ls3,ls4 = splitS(s2)
        def sToInt(s):
            re = 0
            for a in s:
                re = re *26 + ord(a)-ord("A")
            return re
        def intToS(a):
            if a ==0:
                return "A"
            re = ""
            while a >0:
                k = a %26
                re += chr(ord("A")+k)
                a = a //26
            return re
        res =[]
        for i in range(sToInt(ls1),(sToInt(ls3)+1)):
            for j in range(int(ls2),(int(ls4)+1)):
                #print(i,j)
                res.append(intToS(i) + str(j))
        return res

re  = Solution().cellsInRange(s = "K1:L2")

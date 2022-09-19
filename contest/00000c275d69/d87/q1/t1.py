from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        lss = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def getDay(str1):
            ls= str1.split("-")
            a,b = int(ls[0]),int(ls[1])
            #print(a,b,sum(lss[:a]) +b ,sum(lss[:a]) )
            return sum(lss[:a-1]) +b 
        alice =[getDay(arriveAlice) , getDay(leaveAlice)]
        bob =[getDay(arriveBob) , getDay(leaveBob)]
        cnt = 0
        #print(alice,bob)
        for i in range(366):
            if alice[0]<=i<=alice[1] and bob[0]<=i<=bob[1]:
                cnt +=1
        return cnt





re =Solution().countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31")
print(re)
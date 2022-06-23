from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        isLow = any(c.islower() for c in password)
        isBig = any(c.isupper() for c in password)
        isDig =any(c.isdigit() for c in password)
        sc = "!@#$%^&*()-+"
        isSc = any(sc.find(c)>=0 for c in password)
        isLen = len(password) >=8
        isSame = any(password[i] ==password[i-1] for i in range(1,len(password)))
        return isLow and isBig and isDig and isSc and isLen and (not isSame)
    
re =Solution().strongPasswordCheckerII("IloveLe3tcode!")
print(re)
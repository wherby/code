from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels= {'a':0,'e':1,'i':2,'o':3 ,'u':4}
        def check(str):
            ls = [0]*5
            for a in str:
                if a not in vowels:
                    return False
                ls[vowels[a]] +=1
            for a in ls:
                if a == 0:
                    return False
            return True
                
        cnt =0
        n = len(word)
        for i in range(n):
            for j in range(i+5,n+1):
                sb = word[i:j]
                if check(sb):
                    cnt +=1
        return cnt
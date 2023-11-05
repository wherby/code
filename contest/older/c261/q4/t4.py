from collections import defaultdict
from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        dic  = defaultdict(list)
        n = len(s)
        for i in range(n):
            a = s[i]
            o = ord(a) -ord('a')
            dic[o].append(i)
        availble =k - repetition
        
        
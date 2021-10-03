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
        mp={}
        cnt =0
        for i in reversed(range(len(s))):
            if s[i] == letter: cnt +=1
            mp[i] =cnt
        stack =[]
        for i,x in enumerate(s):
            while stack and stack[-1] > x and len(stack) + len(s) -i >k and (stack[-1] !=letter or repetition < mp[i]):
                if stack[-1] == letter:
                    repetition +=1
                stack.pop()
            if len(stack) < k and (x == letter  or len(stack) + repetition <k):
                stack.append(x)
                if x ==letter:
                    repetition -=1
        return "".join(stack)
        

re = Solution().smallestSubsequence("leet",3,"e",2)
print(re)
        
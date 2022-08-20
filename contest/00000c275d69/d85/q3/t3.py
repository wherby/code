import heapq
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        ls=[0]*(n+1)
        for st,e,d in shifts:
            if d ==0:
                ls[st] -=1
                ls[e+1] +=1
            else:
                ls[st] +=1
                ls[e+1] -=1
        ret = ""
        acc =0
        for i in range(n):
            acc += ls[i]
            k = ((ord(s[i]) -(ord('a'))) +acc + 26*10000)%26 
            k = chr(k+ord('a'))
            ret += k
        return ret




re =Solution().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])
print(re)
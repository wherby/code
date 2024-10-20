# slidewindow 

from collections import defaultdict,deque
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt =0
        dic =defaultdict(int)
        l = 0 
        for a in s:
            dic[a] +=1
            while dic[a] >=k:
                dic[s[l]] -=1
                l +=1
            cnt += l 
        return cnt
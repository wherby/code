from collections import defaultdict
from bisect import bisect_right
class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        n = len(persons)
        self.n = n
        self.res =[-1]*n
        self.timeline = times
        mx =0
        mxC = -1
        dic = defaultdict(int)
        for i in range(n):
            c = persons[i]
            dic[c] +=1
            if dic[c]>=mx:
                self.res[i] = c
                mxC = c
                mx = dic[c]
            else:
                self.res[i]= mxC
    
            


    def q(self, t: int) -> int:
        idx = bisect_right(self.timeline,t)
        return self.res[idx-1]


re =TopVotedCandidate([0,0,0,0,1],[0,6,39,52,75])
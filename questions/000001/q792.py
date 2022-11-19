from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ls =[[] for _ in range(26)]
        n = len(s)
        for i,a in enumerate(s):
            k = ord(a)-ord('a')
            ls[k].append(i)
        cnt =0 
        #print(ls)
        for word in words:
            fd =True
            idx = 0 
            for a in word:
                k = ord(a)-ord('a')
                #print(a,k,ls[k])
                idx = bisect_left(ls[k],idx)
                if idx>=len(ls[k]):
                    fd = False
                    break
                else:
                    idx = ls[k][idx]+1
            if fd ==True: cnt +=1
        return cnt

re =Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"])
print(re)
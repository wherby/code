# https://leetcode.cn/contest/weekly-contest-380/problems/find-beautiful-indices-in-the-given-array-ii/
from typing import List, Tuple, Optional
class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.n = n
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod

    def search(self,pattern):
        m = len(pattern)
        ps = StringHash(pattern)
        ph = ps.query(0,m)
        ret = []
        for i in range(self.n-m+1):
            if self.query(i, i+ m) == ph:
                ret.append(i)
        return ret

sh = StringHash("a")
print(sh.query(0,1))

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        sh = StringHash(s)
        aidx =sh.search(a)
        bidx =sh.search(b)
        bidx = [-10**10] +bidx + [10**10]
        m = len(bidx)
        l = 0 
        ret =[]
        
        for ai in aidx:
            while l< m and bidx[l+1]<=ai:
                l +=1
            if abs(ai - bidx[l]) <= k or abs(bidx[l+1] -ai) <=k:
                ret.append(ai)
        return ret
    

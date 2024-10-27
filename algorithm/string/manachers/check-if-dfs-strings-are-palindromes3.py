# 用StringHash
from typing import List, Tuple, Optional


class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:

        n = len(s)
        ans = [None]*n

        time = 0
        g = [[] for _ in range(n)]
        for i,a in enumerate(parent):
            if a>=0:
                g[a].append(i)
        node = [[-1,-1] for _ in range(n)]

        def dfs(idx):
            nonlocal time 
            node[idx][0] = time
            for a in g[idx]:
                dfs(a)
            node[idx][1] = time 
            time +=1
        dfs(0)
        ls = ["*" for _ in range(n)]
        for i,(a,b) in enumerate(node):
            ls[b] = s[i]
        s1 = "".join(ls)
        rs1 =s1[::-1]
        hs = StringHash(s1)
        hrs= StringHash(rs1)
        for i,(a,b) in enumerate(node):
            ans[i] = hs.query(a,b) == hrs.query(n-1-b,n-1-a)
        return ans
        
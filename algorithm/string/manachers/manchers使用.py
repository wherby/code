# https://leetcode.cn/contest/weekly-contest-443/problems/longest-palindrome-after-substring-concatenation-ii/submissions/617063564/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf


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
    def longestPalindrome(self, s: str, t: str) -> int:
        def manachers(S):
            A = "@#" + "#".join(S) + "#$"
            Z = [0] * len(A)
            center = right =0
            for i in range(1,len(A)-1):
                if i < right:
                    Z[i] = min(right -i,Z[2*center -i]) # Z[2*center -i]是 i 关于center的对称点， 因为在[left, right]上对称，则 对称点的对称性是对称的
                while A[i + Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] +=1
                if i + Z[i] > right:
                    center,right = i , i+ Z[i]
            return Z[2:-2:1]
        
        def getMx(s,t,isG):
            re = 1
            sh = StringHash(s)
            tr =t[::-1]
            th = StringHash(tr)
            dic ={}
            dic2 ={}
            m = len(tr)
            for i in range(m):
                for j in range(i,m):
                    dic[th.query(i,j+1)] =j
            #print(dic,tr)
            n = len(s)
            for i in range(n):
                for j in range(i,n):
                    dic2[sh.query(i,j+1)] =i
                    #print(i,j,sh.query(i,j+1))
                    if sh.query(i,j+1) in dic:
                        
                        re = max(re,(j-i+1)*2 + int( (j !=n-1 or dic[sh.query(i,j+1)] !=m-1 ) and isG) )
                        #print(dic[sh.query(i,j+1)],i,j+1)
                        #print(re,j,int( (j !=n-1 or i !=0 ) and isG),j !=n-1 , (j !=n-1 or i !=0 ),int( (j !=n-1 or dic[sh.query(i,j+1)] !=0 ) and isG),(j !=n-1 or dic[sh.query(i,j+1)] !=0 ),dic[sh.query(i,j+1)] )
            zs = manachers(s)
            for i,a in enumerate(zs):
                re = max(re,a)
                if a >1:
                    if i %2 ==1:
                        ed = i //2-a//2+1
                        for k in range(ed):
                            if sh.query(k, ed) in dic:
                                re = max(re,(i//2-k+1)*2)
                    elif isG:
                        ed = i //2-a//2
                        #print(ed)
                        for k in range(ed):
                            #print(sh.query(k,ed),dic,k,ed)
                            if sh.query(k, ed) in dic:
                                re = max(re,(i//2-k+1)*2-1)
            zs2 = manachers(tr)
            #print(zs2,tr)
            for i,a in enumerate(zs2):
                re = max(re,a)
                if a >0:
                    if i %2 ==1:
                        ed = i //2-a//2+1
                        for k in range(ed):
                            if th.query(k, ed) in dic2:
                                re = max(re,(i//2-k+1)*2)
                    elif isG:
                        ed = i //2-a//2
                        for k in range(ed):
                            if th.query(k, ed) in dic2:
                                re = max(re,(i//2-k+1)*2-1)
            return re 
        return getMx(s,t,True)





re =Solution().longestPalindrome(s ="wbrbv", t = "w")
print(re)
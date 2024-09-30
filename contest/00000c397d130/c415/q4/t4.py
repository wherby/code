# https://leetcode.cn/contest/weekly-contest-415/problems/minimum-number-of-valid-strings-to-form-target-i/description/
#  No.3213

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



def calculate_z_array(s):
    N = len(s)
    Z = [0] * N
    L, R = 0, 0
    for i in range(1,N):
        if i < R:
            Z[i] = min(R-i,Z[i-L])

        while i+ Z[i]< N and s[Z[i]]  == s[i+ Z[i]]:
            Z[i] +=1
        if i + Z[i]>R:
            L = i 
            R = i +Z[i] 
    return Z


def z_algorithm(s):
    s = [ord(c) for c in s]
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    j = 0
    for i in range(1, n):
        z[i] = 0 if j + z[j] <= i else min(j + z[j] - i, z[i - j])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if j + z[j] < i + z[i]:
            j = i
    z[0] = n
    return z

from math import ceil, log2

class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basev = 0, basef=lambda x:x):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        self.tree = [0] * ( 2**ceil(log2(len(array))+1) - 1 )
        self.build(array)
    
    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a)-1, 0, a)

    def _query_util(self, i, ln, rn, l, r):
        if ln>=l and rn<=r:
            return self.tree[i]
        if ln>r or rn<l:
            return self.basev
        return self.merge( self._query_util( 2*i+1, ln, (ln+rn)//2, l, r ), self._query_util( 2*i+2, (ln+rn)//2+1, rn, l, r ) )

    def query(self, l, r):
        return self._query_util( 0, 0, self.n-1, l, r )

    def _update_util(self, i, ln, rn, x, v):
        if x>=ln and x<=rn:
            if ln != rn:
                self._update_util( 2*i+1, ln, (ln+rn)//2, x, v )
                self._update_util( 2*i+2, (ln+rn)//2 + 1, rn, x, v )
                self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            else:
                self.tree[i] = self.basef(v)

    def update(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v     

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        dp = [10**10]*(n+1)
        dp[0] = 0
        ls =[0]*(n+1)
        for word in words:
            m = len(word)
            zls = calculate_z_array(word +"#" +target)
            #zls = z_algorithm(word +"#" +target)
            for i in range(n):
                ls[i+zls[m+1+i]] = max(ls[i+zls[m+1+i]],zls[m+1+i])
            #print(zls,word,ls,zls2)
        #print(ls,"a")
        for i in range(n,1,-1):
            ls[i-1] = max(ls[i-1],ls[i]-1)
        #print(ls)
        seg = segment_tree(dp,merge=min,basev=10**10)
        for i in range(1,n+1):
            #print(i,ls[i])
            dp[i] = seg.query(i-ls[i],i) +1
            #print(seg.query(i-ls[i],i) ,i-ls[i],i,)
            seg.update(i,dp[i])
            #print(dp)
        return dp[-1] if dp[-1]< 10**10 else -1
        






#re =Solution().minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc")
#re = Solution().minValidStrings(["b","ccacc","a"],"cccaaaacba")
re = Solution().minValidStrings(["aaaaac","cc","bbbacb","aaabbaccbbcbcacabacacaccbcaacccaacbaacccabbcaacababcaaabcbabcaaaccccabacaccbcaaaabcbcccaccabccababacbabbabababbaaaccaabbbcbbbabbaaccbbababaacbaccbccabaaaabcbaabcabcccbcbabcbccabbaaacabcbbcaaaabcabcbcc"],"cbaaaaaaacbb")
print(re)
#https://leetcode.cn/contest/weekly-contest-411/problems/count-substrings-that-satisfy-k-constraint-ii/submissions/
from typing import List, Tuple, Optional
from collections import defaultdict,deque

class SegTree:
    def __init__(self, arr):
        m = len(arr)
        n = 1
        while n <m:
            n =n<<1
        self.n = n
        self.tree = [0] *(2*n)
        for i in range(m):
            self.tree[n+i] = arr[i]
        for i in range(n-1,0,-1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def sum(self,a,b):
        a += self.n
        b += self.n
        s =0 
        while a<=b:
            #print(a,b)
            if a %2 ==1:
                s+= self.tree[a]
                a+=1
            if b%2 ==0:
                s += self.tree[b]
                b -=1
            a =a //2
            b = b //2
            #print(a,b,s)
        return s
    
    def add(self,k, x):
        k += self.n
        self.tree[k] +=x
        k = k//2
        while k >=1:
            self.tree[k] = self.tree[2*k] + self.tree[2*k+1]
            k= k//2


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        sg1= SegTree([0]*n)
        sg2= SegTree([0]*n)
        m = len(queries)
        ret = [-1]*m
        dic2 = defaultdict(list)
        for i,(a,b) in enumerate(queries):
            dic2[b].append((i,a))
        
        dic = defaultdict(int)
        l = 0 
        for i,a in enumerate(s):
            dic[a] +=1
            while dic["0"] > k and dic["1"]>k:
                sg1.add(l,i-1)
                sg2.add(l,1)
                dic[s[l]] -=1
                l +=1
            for (idx,f) in dic2[i]:
                acc = (i-f+1)*(i-f+2)//2
                #print(acc,idx,f,i,sg2.query(f,i),sg1.query(f,i))
                acc -= sg2.sum(f,i) * i - sg1.sum(f,i)
                ret[idx] = acc
        return ret
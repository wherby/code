# https://www.luogu.com.cn/record/182066065

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "P2801/input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


# https://www.luogu.com.cn/problem/P2801

from typing import List, Tuple, Optional
import math
from bisect import bisect_right,insort_left,bisect_left

class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.bsize = int(math.sqrt(n))+1
        self.m = (n+self.bsize-1)//self.bsize
        self.st = [i*self.bsize for i in range(self.m)]
        self.ed = [(i+1)*self.bsize-1 for i in range(self.m)]   
        self.ed[-1] = n-1
        self.nums = nums
        self.delta =[0]*self.m
        self.setup()
    
    def setup(self):
        self.t = []
        for i in range(self.m):
            t1 = [self.nums[j] for j in range(self.st[i],self.ed[i]+1)]
            t1.sort()
            self.t.append(t1)
    
    def sort(self,x):
        for i in range(self.st[x],self.ed[x]+1):
            self.t[x][i-self.st[x]] = self.nums[i]
        self.t[x].sort()

    def update(self, l,r,c):
        x,y = l//self.bsize,r//self.bsize
        if x ==y:
            for i in range(l,r+1):
                self.nums[i] += c 
            self.sort(x)
        else:
            for i in range(l, self.ed[x]+1):
                self.nums[i] +=c 
            for i in range(self.st[y],r+1):
                self.nums[i] +=c 
            for i in range(x+1,y):
                self.delta[i] +=c 
            self.sort(x)
            self.sort(y)

    def query(self,l,r,z):
        ans = 0
        x,y = l//self.bsize, r //self.bsize
        if x==y:
            for i in range(l,r+1):
                if self.nums[i] + self.delta[x] >=z:
                    ans +=1
        else:
            for i in range(l, self.ed[x]+1):
                if self.nums[i] + self.delta[x] >=z:
                    ans +=1
            for i in range(self.st[y], r+1):
                if self.nums[i] + self.delta[y] >=z:
                    ans +=1
            for i in range(x+1,y):
                ans += self.ed[i] - bisect_left(self.t[i],z-self.delta[i]) +1
        return ans


N,Q = list(map(lambda x: int(x),input().split()))
ls = list(map(lambda x: int(x),input().split()))
ops = []
na = NumArray(ls)
for i in range(Q):
    m,l,r,c = input().split()
    if m == "A":
        print(na.query(int(l)-1,int(r)-1,int(c)))
    else:
        na.update(int(l)-1,int(r)-1,int(c))

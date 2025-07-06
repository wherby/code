# https://leetcode.cn/problems/minimum-stability-factor-of-array/submissions/
# SegQuickversion will AC and others will failed

from typing import List, Tuple, Optional
import math
from functools import cache

@cache
def gcd1(a,b):
    return math.gcd(a,b)

class SegTree:
    def __init__(self, arr,op):
        m = len(arr)
        n = 1
        while n <m:
            n =n<<1
        self.n = n
        self.tree = [0] *(2*n)
        self.op = op
        for i in range(m):
            self.tree[n+i] = arr[i]
        for i in range(n-1,0,-1):
            self.tree[i] = self.op(self.tree[2*i] , self.tree[2*i+1])

    def query(self,a,b):
        a += self.n
        b += self.n
        s =0 
        while a<=b:
            #print(a,b)
            if a %2 ==1:
                s=self.op(s, self.tree[a])
                a+=1
            if b%2 ==0:
                s =self.op(s,self.tree[b])
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
            self.tree[k] =self.op(self.tree[2*k] , self.tree[2*k+1])
            k= k//2

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        t1 =len([a for a in nums if a != 1])
        if t1 -maxC <=0:
            return 0
        n = len(nums)

        st = SegTree(nums,math.gcd)

        lfrom = 0
        dic ={}
        for i in range(n):
            while st.query(lfrom,i) ==1 and lfrom < i:
                lfrom +=1
            dic[i] = lfrom

        #print(dic)
        def verify(md,c):
            lst = -1
            for i in range(n):
                if min(i- dic[i] +1,i-lst) > md:
                    if c:
                        c -=1
                        lst =i
                    else:
                        return False
            return True
        l ,r  = 1, n+1
        r = n //(maxC+1)
        while l < r:
            md = (l+r)>>1
            #rint(md,verify(md,maxC))
            if verify(md,maxC):
                r = md 
            else:
                l = md +1
        return l
import sys
sys.path.append("..")
from input.v5input import nums,maxC
re = Solution().minStable(nums,maxC)
print(re)
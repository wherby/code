
# https://leetcode.cn/contest/biweekly-contest-162/problems/threshold-majority-queries/submissions/649281456/
# 用 buk 记录区间频率的值，O(1)时间更新，其中mx记录最大频率
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
from math import sqrt
INF  = math.inf


class Solution:
    def subarrayMajority(self, nums, queries):
        n=len(nums);B=max(1,int(sqrt(n)))
        idx=sorted(range(len(queries)),key=lambda i:((queries[i][0]//B,queries[i][1]) if (queries[i][0]//B)&1==0 else(queries[i][0]//B,-queries[i][1])))
        cnt=defaultdict(int); buk=[set() for _ in range(n+1)];mx=0
        def add(i):
            nonlocal mx
            x=nums[i];c=cnt[x]
            if c:buk[c].remove(x)
            c+=1;cnt[x]=c;buk[c].add(x);mx=max(mx,c)
        def rm(i):
            nonlocal mx
            x=nums[i];c=cnt[x];buk[c].remove(x)
            if c==1:del cnt[x]
            else:buk[c-1].add(x);cnt[x]=c-1
            while mx and not buk[mx]:mx-=1
        ans=[0]*len(queries);L=R=0;add(0)
        for i in idx:
            l,r,t=queries[i]
            while L>l:L-=1;add(L)
            while R<r:R+=1;add(R)
            while L<l:rm(L);L+=1
            while R>r:rm(R);R-=1
            ans[i]=min(buk[mx]) if mx>=t else -1
        return ans

from input.input import nums,querys
re =Solution().subarrayMajority(nums,querys)
print(re)
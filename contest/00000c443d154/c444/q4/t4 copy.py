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


class Node:
    def __init__(self,key,val):
        self.key =key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self,capacity):
        self.m = {}
        self.capacity = capacity
        self.h = Node(-1,-1)
        self.t = Node(capacity,capacity)
        self.h.next = self.t
        self.t.prev = self.h

    def remove(self, node):
        prev =node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def touch(self,node):
        self.remove(node)
        self.newHead(node)
    
    def newHead(self,node):
        h = self.h.next
        node.next =h 
        h.prev = node
        node.prev = self.h
        self.h.next = node
    
    def get(self,key):
        node = self.m.get(key,None)
        if node:
            self.touch(node)
            return node.val
        return -1

    def put(self,key,val):
        node = self.m.get(key,None)
        if node:
            self.touch(node)
            node.val = val
        else:
            if len(self.m) == self.capacity:
                last = self.t.prev
                self.m.pop(last.key)
                self.remove(last)
            node = Node(key,val)
            self.m[key] = node
            self.newHead(node)

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        sl=SortedList([])
        
        if len(nums) <=1:
            return 0
        if len(nums) ==2 and nums[0] > nums[1]:
            return 1
        n = len(nums)
        ssl =SortedList([])
        for i in range(n-1):
            sl.add((nums[i] + nums[i+1], i,i+2))
            ssl.add(i)
        pre =LRUCache(n)
        for i in range(n):
            pre.put(i,i)
        #print(ssl)
        cnt =0
        dic ={}
        while len(sl) >0:
            print(sl,ssl)
            while sl[0][1] != ssl[0]:
                #print(sl)
                a,b,d =sl[0]
                sl.remove((a,b,d))
                if b in dic or pre.m[b].prev.prev.key !=d  :
                    # c= pre.m[b].prev.k
                    # sl.add((nums[c] + nums[b],b,c))
                    continue
                c=pre.m[b].prev.key
                nums[b]=nums[b]+nums[c]
                cnt +=1
                pre.remove(pre.m[c])
                if c != n-1:
                    ssl.remove(c)
                dic[c] =1
                nums[c] = -10000000
                c = pre.m[b].prev.key
                if pre.m[b].prev.prev != None:
                    d = pre.m[b].prev.prev.key
                    sl.add((nums[b] + nums[c],b,d))
                d = pre.m[b].next.key
                if d != n:
                    if pre.m[b].prev.prev != None:
                        e = pre.m[b].prev.prev.key
                        sl.add((nums[d]+nums[b],d,e))
                print(sl,nums)
            sl.remove(sl[0])
            ssl.remove(ssl[0])
        print(sl)
        return cnt


re =Solution().minimumPairRemoval([-2,1,2,-1,-1,-2,-2,-1,-1,1,1])
print(re)
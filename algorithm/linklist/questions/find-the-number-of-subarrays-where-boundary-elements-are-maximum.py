# https://leetcode.cn/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/submissions/523434102/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Node:
    def __init__(self,key,val):
        self.key =key
        self.val = val
        self.prev = self.next = None 
        
class LinkedList:
    def __init__(self) -> None:
        self.m = {}
        self.h = Node(-1000,0)
        self.t = Node(-1000,0)
        self.h.next = self.t
        self.t.prev = self.h
    
    def __delete__(self, node):
        prev =node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        

    # put the element at beginning
    def newHead(self,node):
        h = self.h.next
        node.next =h 
        h.prev = node
        node.prev = self.h
        self.h.next = node
         
    def put(self,key,val):
        node = self.m.get(key,None)
        if node:
            print("Key existed")
            node.val = val
        else:
            node = Node(key,val)
            self.m[key] = node
            self.newHead(node)
            
    def newTail(self,node):
        t = self.t.prev
        node.prev = t 
        t.next = node 
        node.next = self.t 
        self.t.prev = node 
    
    def append(self,key,val):
        node= self.m.get(key,None)
        if node:
            print("Key existed")
            node.val =val
        else:
            node = Node(key,val)
            self.m[key] =node 
            self.newTail(node)
            
    def removeByKey(self,key):
        node = self.m.get(key,None)
        if not node:
            print("Key not existed:",key,self.m)
        else:
            self.__delete__(node)
            # https://stackoverflow.com/questions/5713218/best-method-to-delete-an-item-from-a-dict
            self.m.pop(node.key) #self.m.pop(node.key,None) will suppressing  error for key not existed

    def listPrint(self,node):
        while node is not None:
            print(node.key,node.val)
            node =node.next


        
class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        sm = 0
        dic = defaultdict(list)
        lls = LinkedList()
        for i,a in enumerate(nums):
            dic[a].append(i)
            lls.append(i,a)
        ts = list(set(nums))
        ts.sort()
        for s in ts:
            acc =0
            for i in dic[s]:
                node = lls.m[i]
                if node.prev.val == s:
                    acc +=1
                else:
                    acc =1
                sm +=acc
            for i in dic[s]:
                lls.removeByKey(i)
        return sm
                        
                
                





re =Solution().numberOfSubarrays([11,57,27,14,57])
print(re)
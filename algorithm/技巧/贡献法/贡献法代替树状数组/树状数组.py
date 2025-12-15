
from typing import List, Tuple, Optional

class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)
        self.bit= [0]*self.n
        for i in range(self.n):
            self.add(i,arr[i])
    
    def sumTo(self, r):
        ret = 0
        while r >=0:
            ret += self.bit[r]
            r = (r&(r+1))-1
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx =  idx | (idx +1)
            

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)

        ls = []
        cur = 0
        lss = set([])
        for i in range(n):
            ls.append(damage[i] + requirement[i] + cur)
            lss.add(cur+hp)
            cur += damage[i]
            lss.add(ls[-1])
            
        lss2 = list(lss)
        lss2.sort()
        dic = {}
        for i,a in enumerate(lss2):
            dic[a] = i
        arr = [0]*(len(lss2)+2)
        for a in ls:
            arr[dic[a]] +=1
        ft = FenwickTree(arr)
        acc= 0
        cur = 0
        for i in range(n):
            acc +=ft.sumTo(dic[cur+hp])
            ft.add(dic[ls[i]],-1)
            cur += damage[i]
        return acc
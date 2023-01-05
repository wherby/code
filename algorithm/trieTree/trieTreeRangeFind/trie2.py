# https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/
from typing import List, Tuple, Optional
class node:
    def __init__(self):
        self.left,self.right = None,None 
        self.path = 0 

class trie:
    def __init__(self,at):
        self.root= node()
        self.at = at

    def insert(self,i):
        curr = self.root 
        for j in range(self.at,-1,-1):
            if not(i &(1<<j)):
                if curr.left == None:
                    curr.left = node()
                curr = curr.left
            else:
                if curr.right ==None:
                    curr.right = node()
                curr = curr.right
            curr.path +=1
    
    def get(self,node):
        if node == None:
            return 0 
        return node.path

    def find(self,curr, i,toValue , at):
        if curr == None:
            return 0 
        if at == -1:
            return self.get(curr)
        b,m = i &(1<<at) , toValue & (1<<at)
        if m ==0:
            if b ==0:
                return self.find(curr.left,i,toValue,at -1)
            else:
                return self.find(curr.right,i,toValue,at -1)
        else:
            if b ==0:
                return self.get(curr.left)  + self.find(curr.right,i,toValue,at-1)
            else:
                return self.get(curr.right) + self.find(curr.left,i,toValue,at -1)

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        t,ans = trie(len(bin(max(nums +[high +1]))) -2),0
        for i in nums:
            ans += t.find(t.root,i,high,t.at) - t.find(t.root,i,low-1, t.at)
            t.insert(i)
        return ans

re = Solution().countPairs(nums = [1,4,2,7], low = 2, high = 6)
print(re)
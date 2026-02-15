# https://leetcode.com/contest/weekly-contest-489/problems/longest-almost-palindromic-substring/description/
from typing import List, Tuple, Optional


from sortedcontainers import SortedDict,SortedList


class TrieNode:
    def __init__(self):
        self.children = {}
        self.max_idx = -1 
class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i+1] = prefix_xor[i] ^ nums[i]
            
        root = TrieNode()
        
        def insert(val, idx):
            node = root
            node.max_idx = max(node.max_idx, idx)
            for i in range(30, -1, -1):
                bit = (val >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
                node.max_idx = max(node.max_idx, idx)

        def query(val, min_idx):
            node = root
            if node.max_idx < min_idx: return 0
            res = 0
            for i in range(30, -1, -1):
                bit = (val >> i) & 1
                target = 1 - bit
                if target in node.children and node.children[target].max_idx >= min_idx:
                    res |= (1 << i)
                    node = node.children[target]
                else:
                    node = node.children.get(bit)
                    if not node: break 
            return res

        sl = SortedList()
        left = 0
        ans = 0
    
        insert(0, 0)
        
        for right in range(n):
            sl.add(nums[right])
        
            while sl[-1] - sl[0] > k:
                sl.remove(nums[left])
                left += 1
            ans = max(ans, query(prefix_xor[right+1], left))
            insert(prefix_xor[right+1], right + 1)
            
        return ans




re =Solution()
print(re)
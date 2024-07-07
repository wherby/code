# https://leetcode.cn/contest/weekly-contest-405/ranking/  	 孙慢慢
# https://leetcode.cn/contest/weekly-contest-405/problems/construct-string-with-minimum-cost/description/
  
from typing import List, Tuple, Optional

class TrieNode:
    def __init__(self):
        self.children = {}
        self.cost = 10**18

    def add(self, word, cost):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.cost = min(node.cost, cost)

    def search(self, word):
        node = self
        ans = []
        for i, c in enumerate(word):
            if c not in node.children:
                break
            node = node.children[c]
            if node.cost != 10**18:
                ans.append([i, node.cost])
        return ans


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:

        root = TrieNode()
        for i in range(len(words)):
            root.add(words[i], costs[i])
        nt = len(target)
        dp = [10**18]*(nt+1)
        dp[nt] = 0

        for i in range(nt-1, -1, -1):
            node = root
            for cur in range(i, nt):
                if target[cur] not in node.children:
                    break
                node = node.children[target[cur]]
                dp[i] = min(dp[i], dp[cur+1] + node.cost)
        if dp[0] == 10**18:
            return -1
        return dp[0]
# https://leetcode.cn/contest/weekly-contest-311/problems/sum-of-prefix-scores-of-strings/
class Trie(object):

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.cnt =0


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for ch in word:
            k = ord(ch) - ord('a')
            if node.children[k] == None:
                node.children[k] = Trie()
            node = node.children[k]
            node.cnt +=1
        node.isEnd = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self
        for ch in word:
            k = ord(ch) - ord('a')
            if node.children[k] == None:
                return False
            node = node.children[k]
        return node.isEnd == True


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self
        cnt =0
        for ch in prefix:
            k = ord(ch) - ord('a')
            if node.children[k] == None:
                return False
            node = node.children[k]
            cnt  += node.cnt
        return cnt
class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        tre = Trie()
        for word in words:
            tre.insert(word)
        ls = [0]*n 
        for i in range(n):
            re = tre.startsWith(words[i])
            ls[i] = re
        return ls
        



re =Solution().sumPrefixScores(  ["abcd"])
print(re)
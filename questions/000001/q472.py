class Trie:
    def __init__(self):
        self.children = [None]*26
        self.isEnd =False
    
    def insert(self,word):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True
    
    def dfs(self,word,start):
        if start == len(word):
            return True
        node =self
        for i in range(start,len(word)):
            node = node.children[ord(word[i]) -ord('a')]
            if node is None:
                return False
            if node.isEnd and self.dfs(word,i +1):
                return True
        return False
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key = len)
        ans = []
        root = Trie()
        for word in words:
            if word == "":
                continue 
            if root.dfs(word,0):
                ans.append(word)
            else:
                root.insert(word)
        return ans

re = Solution().findAllConcatenatedWordsInADict(words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
print(re)
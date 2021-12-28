#https://leetcode-cn.com/submissions/detail/252754098/
class Trie(object):

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


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
        for ch in prefix:
            k = ord(ch) - ord('a')
            if node.children[k] == None:
                return False
            node = node.children[k]
        return True
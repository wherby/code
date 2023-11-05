from collections import Counter 
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wc = Counter(word1)
        wc2 = Counter(word2)
        if wc.keys() != wc2.keys():
            return False
        #print(wc.values(),wc2.values())
        if sorted(wc.values()) != sorted(wc2.values()):
            return False
        return True

re = Solution().closeStrings(word1 = "aa", word2 = "a")
print(re)
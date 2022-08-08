class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        acc = 0
        n = len(word)
        for i,a in enumerate(word):
            if a in "aeiou":
                acc += (i+1)*(n-i)
        return acc
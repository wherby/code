class Solution:
    def countVowels(self, word: str) -> int:
        ls = ['a', 'e', 'i', 'o', 'u']
        n = len(word)
        sm =0
        for i,a in enumerate(word):
            if a in ls:
                sm += (i+1)*(n-i)
        return sm

re = Solution().countVowels("aba")
print(re)
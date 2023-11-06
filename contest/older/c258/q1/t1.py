class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = word.find(ch)
        if ch == -1:
            return word
        else:
            re1 = word[:l+1]
            re = re1[::-1] + word[l+1:]
            return re


a=Solution().reversePrefix("xyxzxe","z")
print(a)
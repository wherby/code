# https://leetcode.cn/problems/find-the-lexicographically-largest-string-from-the-box-i/submissions/589972161/

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends ==1:
            return word
        n = len(word)
        tlen = n-numFriends+1
        ans =""
        for i in range(n):
            l = min(tlen,n-i)
            ans = max(ans, word[i:i+l])
        return ans

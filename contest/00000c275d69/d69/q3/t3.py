from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic =defaultdict(int)
        sm = 0
        for word in words:
            t= ord(word[0])*1024 + ord(word[1])
            trev = ord(word[1])*1024 + ord(word[0])
            if dic[trev]> 0:
                sm +=4
                dic[trev] -=1
            else:
                dic[t] +=1
        for k,v in dic.items():
            if v >0 and k%1024 == k//1024:
                sm +=2
                break
        return sm

re = Solution().longestPalindrome(words = ["cc","ll","xx"])
print(re)
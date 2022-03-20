from collections import Counter
class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        cnt = Counter(list(text))

        if pattern[0] == pattern[1]:
            m = cnt[pattern[0]]
            return m*(m+1) //2 
        cnta = 0
        cntb = cnt[pattern[1]]
        sm1,sm2 =0,0
        for a in text:
            if a == pattern[0]:
                cnta +=1
                sm1 += cntb
            if a == pattern[1]:
                cntb -=1
        ret = max(cnt[pattern[0]],cnt[pattern[1]])
        return sm1 +ret

re = Solution().maximumSubsequenceCount(text = "aaaa", pattern = "aa")
print(re)
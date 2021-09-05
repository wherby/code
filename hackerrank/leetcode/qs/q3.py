#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def sameC(s):
            n = len(s)
            dic1 = {}
            for i in range(n):
                tp = s[i]
                if tp not in dic1:
                    dic1[tp]=1
                else:
                    return False
            return True
        MX =0
        start =0
        end =0
        n = len(s)
        while end< n:
            tps = s[start:end+1]
            if sameC(tps):
                tn =end+1 -start
                if tn > MX:
                    MX = tn
            else:
                for i in range(start,end+1):
                    if s[i] ==s[end]:
                        start = i+1
                        break
            end = end +1
        return MX
s = Solution()
print s.lengthOfLongestSubstring("abcddrdcba")
print s.lengthOfLongestSubstring("aab")
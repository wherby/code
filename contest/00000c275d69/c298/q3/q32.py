import collections
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ct = collections.Counter(s)
        to_ret = ct['0']
        #print(to_ret)
        vt = 0
        n = 1
        for c in s[::-1] :
            c = int(c)
            vt = vt + c * n
            n = n * 2
            if vt > k :
                break
            if c == 1 :
                to_ret += 1
        return to_ret
                
re =Solution().longestSubsequence(s = "00101001000000", k =1)
print(re)
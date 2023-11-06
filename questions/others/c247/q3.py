# TDK count number 先數數 再更新
from collections import defaultdict
class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        ls =[0]*(1<<11)
        ls[0] =1
        cnt =0
        tmp =0
        for a in word:
            k = ord(a) - ord('a')
            tmp = tmp ^ (1<<k)
            cnt += ls[tmp]
            for j in range(10):
                ktmp = tmp ^ (1 <<j)
                cnt += ls[ktmp]
            ls[tmp] +=1

        return cnt

re = Solution().wonderfulSubstrings(word = "aabb")
print(re)
        
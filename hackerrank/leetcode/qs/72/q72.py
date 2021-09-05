#minDistance Distance of String
#https://leetcode.com/problems/edit-distance/discuss/

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        cur = [0]*(m+1)
        for i in range(m+1):
            cur[i]=i
        for j in range(1,n+1):
            pre = cur[0];
            cur[0] =j
            for i in range(1,m+1):
                temp = cur[i]
                if word1[i-1] == word2[j-1]:
                    cur[i] =pre;
                else:
                    cur[i] = min(pre + 1, cur[i] +1,cur[i-1] +1);
                    pre = temp
        return cur[m]






s= Solution()
print s.minDistance("abcd","ad")
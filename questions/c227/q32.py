
class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n1 = len(word1)
        n2 = len(word2)
        idx1 = 0
        idx2 = 0
        def compare(idx1,idx2):
            q1 =ord(word1[idx1]) if idx1<n1 else 0
            q2 = ord(word2[idx2]) if idx2<n2 else 0
            if q1 == q2 and q1 ==0:
                return True
            if q1 == q2:
                return compare(idx1 +1, idx2 +1)
            return q1 > q2
        k =0
        res = [0]*(n1+n2)
        while k < n1+n2:
            t =""
            if compare(idx1,idx2):
                t=word1[idx1]
                idx1 +=1
            else:
                t=word2[idx2]
                idx2 +=1
            res[k]=t
            k +=1
        re = "".join(res)
        #print(re)
        return re

re = Solution().largestMerge(word1 = "abcabc", word2 = "abdcaba")

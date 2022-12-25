# https://leetcode.cn/problems/largest-merge-of-two-strings/submissions/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ret = ""
        tmp1,tmp2 ="",""
        n1,n2 = len(word1),len(word2)
        i1,i2 = 0,0 
        while i1<n1 or i2 <n2:
            if i1<n1 and word1[i1:] > word2[i2:]:
                ret+=word1[i1]
                i1 +=1
            else:
                ret+=word2[i2]
                i2 +=1
        return ret


class Solution(object):
    def largestMerge(self, a, b):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res =""
        while a and b:
            if a>b:
                res +=a[0]
                a =a[1:]
            else:
                res +=b[0]
                b =b[1:]
        return res +a + b
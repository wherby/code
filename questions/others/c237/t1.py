#https://leetcode.com/contest/weekly-contest-237/problems/check-if-the-sentence-is-pangram/
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        ls = [0] *100
        for s in sentence:
            t = ord(s)-ord('a')
            ls[t] +=1
        for i in range(26):
            if ls[i] ==0:
                return False
        return True
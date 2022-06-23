class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        n = len(answerKey)
        left,right =0,0
        t,f = 0,0
        res = k
        for i in range(n):
            if answerKey[i] == "T":
                t +=1
            else:
                f +=1
            while t >k and f >k:
                if answerKey[left] == "T":
                    t -=1
                else:
                    f -=1
                left +=1
            right =i
            res = max(res,right -left+1)
        return res
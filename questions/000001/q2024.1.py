
class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        n  = len(answerKey)
        def maxLenC(ch):
            remains =k
            left =0
            mxl = k
            for i in range(n):
                if answerKey[i] != ch:
                    remains -=1
                    while remains<0:
                        if answerKey[left] != ch:
                            remains +=1
                        left +=1
                mxl = max(mxl, i-left+1)
            return mxl
        mxl =max( maxLenC("T"),maxLenC("F"))
        return mxl

re = Solution().maxConsecutiveAnswers("TFFT",1)
print(re)
    
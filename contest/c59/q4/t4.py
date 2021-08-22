#https://leetcode.com/problems/number-of-ways-to-separate-numbers/discuss/1417621/Almost-no-one-solved-this
class Solution:

    def helper(self,num,prev,preLen):
        CNST= 10**9+7
        if num[0] =='0':
            return 0
        n = len(num)
        totComb =0
        if len(num )< preLen:
            return 0
        val = int(num)
        if val < prev:
            return 0
        else:
            totComb =1
        
        for i in range(n-1,0,-1):
            if i < preLen:
                return totComb
            val = int(num[:i])
            if val < prev:
                return totComb
            res = self.helper(num[i:],val,i)
            totComb += res%CNST
        return (totComb % CNST)
        
    def numberOfCombinations(self, num) :
        if num[0] =='0':
            return 0
        return self.helper(num, 0,0)
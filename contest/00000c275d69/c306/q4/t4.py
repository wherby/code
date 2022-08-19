class NumCount:
    def __init__(self,N):
        self.ls =[]
        while N>0:
            self.ls.append(N%10)
            N = N//10
        self.ls=self.ls[::-1]
    
    def countfunction(self,l,idx):
        return 10**l
    
    ## count all combination with lenth L
    def countWithNumberOfDigital(self,L):
        count =0
        for i in range(1,10):
            count +=self.countfunction(L-1) 
        return count
    
    def countNumberWithPrefix(self,digital_index,isFirstDigit):
        if digital_index ==len(self.ls):
            return 1 
        if isFirstDigit:
            digitalStart =1
        else:
            digitalStart =0
        count =0
        for digit in range(digitalStart,self.ls[digital_index]):
            count +=self.countfunction(len(self.ls)-digital_index-1)
        count += self.countNumberWithPrefix(digital_index+1,isFirstDigit=False)
        return count
    
    def count(self):
        digtallen = len(self.ls)
        if len(self.ls) ==0:
            return 0
        count = 0
        for L in range(1,digtallen):
            count += self.countWithNumberOfDigital(L)
        count += self.countNumberWithPrefix(0,True)
        return count

class Solution(object):
    def countSpecialNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """




re =Solution()
print(re)
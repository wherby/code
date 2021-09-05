#https://leetcode.com/contest/weekly-contest-61/problems/monotone-increasing-digits/

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <10: 
            return N
        num,n,inv = [],N,-1
        while n>0:
            num.append(n%10)
            n = n /10
        
        for i  in range(len(num)-1,0,-1):
            if num[i] > num[i-1]: 
                inv = i
                while inv < len(num)-1 and num[inv] ==num[inv +1]:
                    inv = inv +1
                break
        if inv == -1:
            return N
        num[inv] = num[inv]-1
        for i in range(inv):
            num[i] = 9
        num = num[::-1]
        re =0
        for i in range(len(num)):
            re = re *10 + num[i]
        return re

s= Solution()
print s.monotoneIncreasingDigits(232)
print s.monotoneIncreasingDigits(10)
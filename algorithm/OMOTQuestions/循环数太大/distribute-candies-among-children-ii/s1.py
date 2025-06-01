
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        acc= 0
        for i in range(min(limit,n)+1):
            res = n-i
            acc += max(0,min(limit,res) +1- max(0,res -limit) )
            #print(i,res,acc,max(limit,res) - max(0,res -limit),max(limit,res) , max(0,res -limit))
        return acc
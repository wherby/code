class Solution(object):
    def findNthDigit(self, n):
        ls =[9*(i+1)* (10**i) for i in range(20)]
        #print(ls[:10])
        idx = 0
        sm = ls[0]
        while n > sm:
            idx +=1
            sm +=ls[idx]
        #print(idx,sm)
        pre = n -(sm -ls[idx])
        nth = (pre+idx) //(idx+1)
        k =   pre %(idx+1) 
        txt = nth + (10 **idx -1)
        #print(k)
        return int(str(txt)[k-1])


re = Solution().findNthDigit(3)
print(re)
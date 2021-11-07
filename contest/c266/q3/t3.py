class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        l=0 
        r =10000000
        if n==1:
            return quantities[0]
        def myDiv(a,b):
            if b == 0:
                return 100000000000000
            if a %b ==0:
                return a//b
            else:
                return a//b +1
        def getNum(a):
            cnt = 0
            for q in quantities:
                re = myDiv(q,a)
                cnt += re
            return cnt
        while l <r :
            mid =(l+r)>>1
            #print(mid)
            cnt = getNum(mid)
            if cnt <=n:
                r= mid
            else:
                l =mid+1
        return l

re =Solution().minimizedMaximum(n = 6, quantities = [11,6])
print(re)
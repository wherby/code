class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        c2 = str(bin(num2)).count('1')
        c1 = str(bin(num1)).count('1')
        c1mask = str(bin(num1))[2:]
        c1len = len(c1mask)
        ret =[0]*c1len
        if c2 > c1len:
            ret =[0]*(c2-c1len) + ret
        for i,a in enumerate(c1mask):
            if a =="1":
                if c2 >0:
                    ret[c1len-1-i] = 1
                    c2 -=1
        idx = 0
        while c2 >0:
            if ret[idx] == 0:
                ret[idx] =1
                c2 -=1
            idx +=1
        ret =  ret[::-1]
        acc = 0 
        for a in ret:
            acc = acc*2 +a
        return acc




re =Solution().minimizeXor(1,7)
print(re)
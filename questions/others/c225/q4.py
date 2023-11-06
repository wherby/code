from bisect import bisect_left
class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        NC= 2000
        ls = [0]*NC
        for i in range(1,NC):
            ls[i] = ls[i-1] +i
        pre= [0]*NC
        for i in range(1,NC):
            pre[i] = pre[i-1] +ls[i]
        #print(pre[-1])
        res =0
        sq =[0]*10000
        for i in range(10000):
            sq[i] = i*(i+1)//2
        #print(sq[-1])
        idx =bisect_left(pre,n)
        if n != pre[idx]:
            num = n- pre[idx-1]
            res += ls[idx-1]
            idx2 = bisect_left(sq,num)
            res +=idx2
        else:
            n =0
            res += ls[idx]
        return res

re = Solution().minimumBoxes(15)
print(re)
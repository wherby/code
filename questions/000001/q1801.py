
from sortedcontainers import SortedDict,SortedList

class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        bs,ss =SortedList(),SortedList()
        for a,b,t in orders:
            if t == 0:
                while len(ss)>0  and b>0 and ss[0][0] <= a:
                    c1,m1 =ss.pop(0)
                    if m1 == b :
                        b =0 
                    elif m1 >b:
                        m1 = m1-b 
                        ss.add((c1,m1))
                        b =0
                    else:
                        b= b-m1 
                if b !=0:
                    bs.add((a,b))
            else:
                while len(bs) >0 and b>0 and bs[-1][0]>=a:
                    c1,m1 = bs.pop()
                    if m1 == b :
                        b = 0 
                    elif m1 >b :
                        m1=m1-b 
                        bs.add((c1,m1))
                        b=0
                    else:
                        b= b -m1 
                if b !=0:
                    ss.add((a,b))
        cnt = 0
        mod =10**9+7
        for _,a in ss:
            cnt +=a 
        for _,a in bs:
            cnt +=a 
        cnt%=mod 
        return cnt

re =Solution().getNumberOfBacklogOrders([[26,7,0],[16,1,1],[14,20,0],[23,15,1],[24,26,0],[19,4,1],[1,1,0]])
print(re)
                    
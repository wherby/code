class MyCalendarTwo(object):


    def __init__(self):
    	self.lst=[[0,9999999999,0]]
     
    def updateSeg(self, a,b,x,sgs):
        n = len(sgs)
        re = []
        for i in range(n):
            if a == b :
                pass
            sgt = sgs[i]
            xt,yt,xvt = sgt
            if a >= yt or b<=xt:
                re.append(sgt)
            elif a > xt :
                if b >yt:
                    re.append([xt,a,xvt])
                    re.append([a,yt,xvt+x])
                    a = yt
                elif b == yt:
                    re.append([xt,a,xvt])
                    re.append([a,yt,xvt+x])
                else :
                    re.append([xt,a,xvt])
                    re.append([a,b,xvt+x])
                    re.append([b,yt,xvt])
            elif a ==xt:
                if b >=yt:
                    re.append([a,yt,xvt+x])
                    a =yt
                else:
                    re.append([a,b,xvt+x])
                    re.append([b,yt,xvt])
        return re   

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.lst) == 0:
            self.lst = [[start,end,1]]
            return True
        tpls = self.lst
        rtp = self.updateSeg(start,end,1,self.lst)
        for item in rtp:
            start,end,va = item
            if va >=3:
                return False
        self.lst= rtp
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
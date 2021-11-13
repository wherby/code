from sortedcontainers import SortedDict,SortedList
class MKAverage(object):

    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        self.idx = 0
        self.ls =SortedList()
        self.inputs = SortedDict()
        self.m = m
        self.k =k
        self.total = 0
        self.minls=SortedList()
        self.maxls =SortedList()


    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        self.idx +=1
        self.inputs[self.idx] = num
        if self.idx > self.m:
            t = self.inputs[self.idx-self.m]
            if t< self.ls[0]:
                self.minls.discard(t)
            elif t > self.ls[-1]:
                self.maxls.discard(t)
            else:
                self.ls.discard(t)
                self.total -=t
        #print(self.minls,self.ls,self.maxls)
        if len(self.ls) ==0:
            self.minls.add(num)
            self.adjust()
        else:
            if num < self.ls[0]:
                self.minls.add(num)
            if num > self.ls[-1]:
                self.maxls.add(num)
            if num>= self.ls[0] and num <= self.ls[-1]:
                self.ls.add(num)
                self.total += num
            self.adjust()
        #print("after")
        #print(self.minls,self.ls,self.maxls)
    def adjust(self):
        if len(self.minls)>self.k:
            t = self.minls[-1]
            self.minls.discard(t)
            self.ls.add(t)
            self.total +=t
        if len(self.maxls) >self.k:
            t = self.maxls[0]
            self.maxls.discard(t)
            self.ls.add(t)
            self.total +=t
        if len(self.ls) > self.m -2*self.k:
            if len(self.minls) <self.k:
                t = self.ls[0]
                self.ls.discard(t)
                self.total -=t
                self.minls.add(t)
            else:
                t = self.ls[-1]
                self.ls.discard(t)
                self.total -=t
                self.maxls.add(t)
        


    def calculateMKAverage(self):
        """
        :rtype: int
        """
        if self.idx< self.m:
            return -1
        #print(self.minls,self.ls,self.maxls)
        return self.total //(self.m-2*self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
#["MKAverage","addElement","addElement","calculateMKAverage","addElement","addElement","calculateMKAverage","addElement","addElement","calculateMKAverage","addElement"]
#[[3,1],[58378],[34909],[],[94574],[29985],[],[77484],[13400],[],[41607]]
obj = MKAverage(3,1)
obj.addElement(58378)
obj.addElement(34909)
obj.addElement(94574)
obj.addElement(29985);  
re=obj.calculateMKAverage()
print(re)
obj.addElement(5);  
obj.addElement(5);  
re=obj.calculateMKAverage()
print(re)
from bisect import bisect_right,bisect_left
from sortedcontainers import SortedList

class DiscreteMax():
    def __init__(self):
        self.ls=SortedList([(0,0)])
    
    def insert(self, idx,val):
        k = bisect_left(self.ls,(idx,0))
        if k == len(self.ls):
            if val >self.ls[-1][1]:
                self.ls.add((idx,val))
        else:
            if val >self.ls[k-1][1]:
                removed=[]
                for i in range(k,len(self.ls)):
                    if val > self.ls[i][1]:
                        removed.append(self.ls[i])
                #print(removed,k)
                for item in removed:
                    self.ls.remove(item)
                self.ls.add((idx,val))
    
    def query(self,idx):
        k = bisect_right(self.ls,(idx,10**19))
        return self.ls[k-1][1]

dm  = DiscreteMax()
dm.insert(1,1)
dm.insert(2,2)
dm.insert(3,3)
print(dm.ls)
print(dm.query(2))
dm.insert(10,10)
print(dm.ls)
print(dm.query(5))
dm.insert(4,4)
dm.insert(6,6)
print(dm.query(5))
print(dm.query(11))
dm.insert(2,12)
print(dm.ls)
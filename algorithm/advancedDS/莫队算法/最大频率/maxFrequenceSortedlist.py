from collections import defaultdict,deque
from sortedcontainers import SortedDict,SortedList
class MaxFreq():
    def __init__(self):
        self.mx = 0
        self.fdict = defaultdict(SortedList)
        self.dic = defaultdict(int)
    
    def add(self,a):
        if self.dic[a] !=0:
            self.fdict[self.dic[a]].remove(a)
        self.dic[a] +=1
        self.fdict[self.dic[a]].add(a)
        self.mx = max(self.mx,self.dic[a])
    
    def remove(self,a):
        self.fdict[self.dic[a]].remove(a)
        if len(self.fdict[self.dic[a]]) == 0 and self.mx ==self.dic[a]:
            self.mx -=1
        self.dic[a] -=1
        self.fdict[a].add(a)
     
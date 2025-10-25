from collections import defaultdict,deque
class FreqTracker():
    def __init__(self):
        self.freq = defaultdict(int)
        self.dic = defaultdict(int)
    
    def modify(self, a,delta):
        aF = self.dic[a]
        self.freq[aF] -=1
        naF = aF + delta
        self.dic[a] = naF
        self.freq[naF] +=1
    
    def freqChecker(self):
        ret = acc = -self.freq[0]
        idx = 1
        while idx <=ret:
            acc -= self.freq[idx]
            ret = min(ret,acc+idx)
            idx +=1
        return ret

frt= FreqTracker()
for i in range(1,20):
    for j in range(i):
        frt.modify(i + 1000,1)
print(frt.freqChecker())
for i in range(1,20):
    for j in range(i):
        frt.modify(i + 1000,1)

print(frt.freqChecker())
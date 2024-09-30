# from ./pic/stringHash.png 
# Verified in contest/00000c397d130/c415/q3/t3.binarySearch.py
class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod
    

sh = StringHash("abcdefg")
print(sh.query(0,7))
print(sh.hls,sh.pls)
# 左闭右开
print(sh.query(0,1))
# from ./pic/stringHash.png
# Add Random https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/2917929/ac-zi-dong-ji-pythonjavacgo-by-endlessch-hcqk/
# Fix from algorithm/string/stringHash/wrongVersion/stringHash.v2 .wrong.py

from random import randint
MOD = randint(8 * 10 ** 8, 9 * 10 ** 8)
class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%MOD
            self.pls[i+1] = (self.pls[i]*131)%MOD
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % MOD) % MOD
    

sh = StringHash("abcdefg")
print(sh.query(0,7))
print(sh.hls,sh.pls)
print(sh.query(0,1))
print(sh.query(0,0))
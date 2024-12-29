# https://leetcode.cn/problems/find-the-lexicographically-largest-string-from-the-box-i/submissions/590030610/
class StringHash:
    def __init__(self,s1):
        self.s1 =s1
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod
    
    def compare(self,a,al,b,bl):
        ml = min(al,bl)
        if self.query(a,a+ml) == self.query(b,b+ml):
            if al == bl:
                return 0 
            if al >bl:
                return 1 
            else:
                return -1
        else:
            if ml <4:
                if self.query(a,a+ml) < self.query(b,b+ml):
                    return -1
                else:
                    return 1
            mlh = ml//2
            if self.query(a,a+mlh) !=self.query(b,b+mlh):
                return self.compare(a,mlh,b,mlh)
            else:
                return self.compare(a+mlh,ml-mlh,b+mlh,ml-mlh)
           
            
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends ==1:
            return word
        n = len(word)
        tlen = n-numFriends+1
        ans =(0,tlen)
        hs = StringHash(word)
        for i in range(n):
            l = min(tlen,n-i)
            if hs.compare(i,l,ans[0],ans[1])>0:
                ans = (i,l)
        return word[ans[0]:ans[0]+ans[1]]
    
re =Solution().answerString("cgwzebexlahnfqsetbeaybmfdzywpvehjybpwiotnciddjonfi",21)
print(re)
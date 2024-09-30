

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        c = bin(x)[2:]
        t = bin(n-1)[2:]
        ls =[0]*64
        for i,a in enumerate(c[::-1]):
            ls[i] =int(a)
        idx =0
        #print(t,ls)
        for b in t[::-1]:
            while ls[idx] ==1:
                idx +=1
            #print(b,idx,ls)
            ls[idx] = int(b)
            idx +=1
        acc =0 
        for a in ls[::-1]:
            acc = acc*2 +a 
        return acc


re = Solution().minEnd(6715154,7193485)
print(re)
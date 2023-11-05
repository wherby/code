import collections
class Solution(object):
    def minCharacters(self, a, b):
        lsa = [0]*26
        lsb = [0]*26
        for t in a:
            i = ord(t) -ord('a')
            lsa[i] +=1
        for t in b:
            i = ord(t)-ord('a')
            lsb[i] +=1
        n = len(a+b)
        ca =n
        cb =n
        cc =n
        for c in range(25):
            na =0
            nb =0
            for i in range(c+1,26):
                na +=lsa[i]
                nb +=lsb[i]
            for i in range(c+1):
                na +=lsb[i]
                nb += lsa[i]
            ca =min(ca,na)
            cb = min(cb,nb)
        for i in range(26):
            nc = n -lsa[i]-lsb[i]
            cc = min(nc,cc)
        print(ca,cb,cc)
        return min(ca,cb,cc)


re = Solution().minCharacters("aba","caa")
print(re)
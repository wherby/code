import collections
class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        lsa =[0]*len(a)
        lsb =[0]*len(b)
        for i in range(len(a)):
            lsa[i] =  ord(a[i]) - ord('a')
        for i in range(len(b)):
            lsb[i] = ord(b[i])- ord('a')
        sa = collections.Counter(lsa)
        sb =collections.Counter(lsb)
        sc = collections.Counter(lsa +lsb)
        na =len(b) +len(a)
        nb = len(b) + len(a)
        n =len(a) +len(b)
        tc =n
        for c in range(25):
            ta=0
            tb=0
            
            for k,v in sa.items():
                if k >c:
                    ta +=v
                else:
                    tb +=v
            for k,v in sb.items():
                if k<=c:
                    ta +=v
                else:
                    tb +=v
            
            na = min(ta,na)
            
            nb =min(tb,nb)
        for c in range(26):
            if c in sc:
                tc = min(tc,n-sc[c])
        print(na,nb,tc)
        return min(na,nb,tc)
       

re = Solution().minCharacters("a","aabcdefghijklmnopqrstuvwxyz")
print(re)
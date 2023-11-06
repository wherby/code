from collections import defaultdict
class Solution(object):
    def sampleStats(self, count):
        n = len(count)
        a1=a2=a3=a4=a5 =-1
        sm =0
        mx=0
        cnt = sum(count)
        idx =0
        need =[]
        if cnt %2 ==0:
            need= [cnt//2 ,cnt //2 +1]
        else:
            need = [cnt//2+1]
        res =[]
        for i in range(n):
            if count[i]  != 0 and a1==-1:
                a1  =i
            if count[i] !=0:
                a2 = i
            sm += i* count[i]
            if mx < count[i]:
                mx = count[i]
                a5=i
            idxnext =idx + count[i]
            for n in need:
                if n > idx and n <=idxnext:
                    res.append(i)
            idx = idxnext
        a3 = sm *1.000 /cnt
        a4 = sum(res) *1.000 /len(res)
        return [a1,a2,a3,a4,a5]
                
from collections import defaultdict,deque

class SubStringCompare:
    def __init__(self,word) -> None:
        self.word =word
        self.stDic ={}
        self.stringCompare(word)
    
    def getKeyOrder(self, dic):
        keys =list(dic.keys())
        keys.sort()
        ret ={}
        for i,k in enumerate(keys):
            for a in dic[k]:
                ret[a] = i
        return ret

    def stringCompare(self, word):
        n = len(word)
        def ord(mid):
            dic = defaultdict(list)
            if mid ==1:
                dic = defaultdict(list)
                for i,a in enumerate(word):
                    dic[a].append(i)
                self.stDic[mid] = self.getKeyOrder(dic)
            else:
                hf = mid//2
                dic = defaultdict(list)
                for i in range(n-mid +1):
                    a = self.stDic[hf][i]
                    b = self.stDic[hf][i+hf]
                    k = a *1000+b 
                    dic[k].append(i)
                self.stDic[mid] = self.getKeyOrder(dic)
        cur = 1
        while cur <= n:
            ord(cur)
            cur =cur*2

    def queryLength(self,tlen):
        n = len(self.word)
        cand= {}
        for i in range(n):
            cand[i] = 0
        acc =0
        for i in range(30,-1,-1):
            if (1<<i)& tlen:
                tmp =defaultdict(list)
                for j in range(n-tlen+1):
                    tmp[cand[j]*n + self.stDic[1<<i][j+acc]].append(j)
                cand= self.getKeyOrder(tmp)
                acc += 1<<i
        return cand
    

re = SubStringCompare("abcdz" *100)

print(re.queryLength(7))
print(max(re.queryLength(7).keys()))

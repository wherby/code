import copy
class Solution(object):
    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ls1 =[]
        ls2 =[]
        def parseString(s):
            n = len(s)
            res =[]
            tp =""
            for a in s:
                if a >= 'a' and a <='z':
                    if len(tp) >0:
                        res.append(tp)
                        tp=""
                    res.append(a)
                else:
                    tp += a
            if len(tp)>0:
                res.append(tp)
            return res
        def addNum(res,k,a):
            for i in range(len(res)):
                res[i][0] +=k
                res[i][1][res[i][0]]=a
            return res
        
        def dp(s1,res,tpv):
            if len(s1) == 0:
                res[tpv] =1
                return res
            for i in range(len(s1)):
                t1 = dp(s1[i+1:],res,tpv +int(s1[:i+1]))
                for t2,v in t1.items():
                    res[t2] =1
            return res
        def addList(res,list):
            rt =[]
            for a in list:
                t2= copy.deepcopy(res)
                t1= addNum(t2,a,"*")
                rt =rt +t1
            return rt
        def getNum(ls):
            cnt = [[0,{}]]
            for a in ls:
                if len(a) ==1:
                    if a >='a' and a<='z':
                        cnt=addNum(cnt,1,a)
                    else:
                        cnt =addNum(cnt,int(a),"*")
                else:
                    d1 = dp(a,{},0)
                    ls4 =[]
                    for k,v in d1.items():
                        ls4.append(k)
                    #print(ls4)
                    cnt = addList(cnt,ls4)
                # if len(cnt) <100:
                #     print(cnt)
                # else:
                #     return cnt
                dic ={}
                for c in cnt:
                    dic[c[0]] =c[1]
                r1 =[]
                for k,v in dic.items():
                    r1.append([k,v])
                cnt =r1
            return cnt
        ls1= parseString(s1)
        ls2 =parseString(s2)
        print(ls1,ls2)
        cand1 = getNum(ls1)
        cand2 = getNum(ls2)
        dic = {}
        def check(d1,d2):
            for k,v in d1.items():
                if v != "*" and k in d2:
                    if d2[k] != "*" and d2[k] != v:
                        return False
            return True
        for c in cand1:
            dic[c[0]] = c[1]
        for c in cand2:
            if c[0] in dic:
                return check(c[1],dic[c[0]])
        return False
                
s1 = "v375v736v443v897v633v527v781v121v317"

s2 = "475v899v753v784v438v415v431v216v968"
re = Solution().possiblyEquals(s1,s2)
print(re)


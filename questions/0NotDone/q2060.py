#https://leetcode.com/contest/weekly-contest-265/problems/check-if-an-original-string-exists-given-two-encoded-strings/
# handle the getNum and dfs for compare
import functools
class Solution(object):
    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
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
        ls1 =parseString(s1)
        ls2 =parseString(s2)
        #print(ls1,ls2)
        
        def getNum(ls):
            res =[int(ls)]
            if len(ls) == 1:
                return res
            if len(ls) ==2:
                if ls[1] != '0':
                    res.append(int(ls[0]) + int(ls[1]))
            if len(ls) ==3:
                if ls[1] != '0':
                    res.append(int(ls[0])+int(ls[1:]))
                if ls[1] != '0' and ls[2] !='0':
                    res.append(int(ls[0]) + int(ls[1]) + int(ls[2]))
                if ls[2] != '0':
                    res.append(int(ls[:2]) + int(ls[2]))
            return res
        
        @functools.lru_cache(None) 
        def compare(i,j,diff):
            if i == len(ls1) and j == len(ls2) and diff ==0:
                return True
            if diff == 0:
                if i == len(ls1) or j == len(ls2):
                    return False
                if ls1[i][0].isalpha() and ls2[j][0].isalpha():
                    if ls1[i] == ls2[j]:
                        return compare(i+1,j+1,diff)
                    else:
                        return False
                else:
                    if ls1[i][0].isalpha() and ls2[j][0].isdigit():
                        ls = getNum(ls2[j])
                        for t in ls:
                            re = compare(i+1,j+1,1-t)
                            if re == True:
                                return True
                        return False
                    elif ls1[i][0].isdigit() and ls2[j][0].isalpha():
                        ls = getNum(ls1[i])
                        for t in ls:
                            re = compare(i+1,j+1,t-1)
                            if re == True:
                                return True
                        return False
                    else:
                        ls3 = getNum(ls1[i])
                        ls4 = getNum(ls2[j])
                        for t1 in ls3:
                            for t2 in ls4:
                                re = compare(i+1,j+1,t1-t2)
                                if re == True:
                                    return True
                        return False
            elif diff >0:
                if j == len(ls2):
                    return False
                if ls2[j][0].isalpha():
                    return compare(i,j+1,diff -1)
                else:
                    ls = getNum(ls2[j])
                    for t in ls:
                        re = compare(i,j+1,diff-t)
                        if re == True:
                            return True
                    return False
            else:
                if i == len(ls1):
                    return False
                if ls1[i][0].isalpha():
                    return compare(i+1,j,diff +1)
                else:
                    ls = getNum(ls1[i])
                    for t in ls:
                        re = compare(i+1,j,diff +t)
                        if re == True:
                            return True
                    return False
        res = compare(0,0,0)
        #print(res)
        return res
        


s1 = "v375v736v443v897v633v527v781v121v317"

s2 = "475v899v753v784v438v415v431v216v968"
re = Solution().possiblyEquals(s1,s2)
print(re)

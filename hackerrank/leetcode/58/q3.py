#https://leetcode.com/problems/number-of-atoms/description/
#Tag: Stack for expression compute
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def evalEle(Ele):
            name = ""
            num =0
            for i in Ele:
                if i >="0" and i <="9":
                    num = num*10 + ord(i)-ord('0')
                else:
                    name = name + i
            if num == 0:
                num =1
            return [name,num]
        def evalNum(Num):
            num =0
            for i in Num:
                num = num*10 + ord(i)-ord('0')
            return num
        def mulEles(ls,num):
            re = []
            for t1 in ls:
                ele,num1 = t1
                re.append([ele,num1*num])
            return re
        re = []
        tps=""
        n =len(formula)
        for i in range(n):
        	tp = formula[i]
        	if tp >="A" and tp <="Z":
        		if tps != "":
        			re.append(tps)
        		tps = tp
        	if tp=="(" or tp ==")":
        		if tps !="":
        			re.append(tps)
        		re.append(tp)
        		tps = ""
        	if tp>="a" and tp <="z":
        		tps =tps + tp
        	if tp>="0" and tp <="9":
        		tps = tps +tp
        re.append(tps)
        #print re
        stak1=[[]]
        for t1 in re:
            if t1[0]>="A" and t1[0]<="Z":
                re =evalEle(t1)
                stak1[-1].append(re)
            if t1[0] == "(":
                stak1.append([])
            if t1[0] ==")":
                pass
            if t1[0] >="0" and t1[0]<="9":
                re = evalNum(t1)
                last = stak1.pop()
                re2 = mulEles(last,re)
                stak1[-1].extend(re2)
        dic1 ={}
        for t1 in stak1[0]:
            ele,num = t1
            if ele not in dic1:
                dic1[ele] =num
            else:
                dic1[ele] = dic1[ele] +num
        keys = sorted(dic1.keys())
        re=""
        for key in keys:
            re=re + key
            num = dic1[key]
            if num != 1:
                re = re + str(num)
        return re 
                





s = Solution()
s.countOfAtoms("K4(ON(SO3)2)2")
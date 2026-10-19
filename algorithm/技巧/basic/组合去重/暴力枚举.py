
import itertools
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        acc =0 
        left=right = 0 
        lls ,rls = [],[]
        for i,a in enumerate(s):
            if a =="(":
                acc +=1
                lls.append(i)
            elif a ==")":
                rls.append(i)
                if acc ==0:
                    right +=1
                else:
                    acc -=1
        left = acc 
        leftSelect = []
        if left ==0:
            leftSelect = [[]]
        else:
            for a in itertools.combinations(lls,left):
                leftSelect.append(list(a))
        rightSelect = []
        if right ==0:
            rightSelect = [[]]
        else:
            for a in itertools.combinations(rls,right):
                rightSelect.append(list(a))
        ret = set()
        #print(left,right,leftSelect,rightSelect)
        for a in leftSelect:
            for b in rightSelect:
                c = set(a+b)
                tmp = []
                cur = 0
                isG = True
                for i,ch in enumerate(s):
                    if i not in c:
                        if ch =="(":
                            cur +=1
                        if ch ==")":
                            cur -=1
                        if cur <0:
                            isG =False 
                            break 
                        tmp.append(ch)
                if isG:
                    ret.add("".join(tmp))
                #print(a,b,c,isG,tmp)
        return list(ret)
from typing import List, Tuple, Optional

def midToPost(arr,ordDic):
    res =[]
    st =[]
    for a in arr:
        if a not in ordDic:
            res.append(a)
        else:
            if a =="{":
                st.append(a)
            elif a == "}":
                while st and st[-1] !="{":
                    res.append(st[-1])
                    st.pop()
                    
                st.pop()
            else:
                while st and ordDic[st[-1]]>= ordDic[a]:
                    k = st.pop()
                    res.append(k)
                st.append(a)
        #print(a,st,res)
    while st:
        res.append(st.pop())
    return res

ordDic = {"{":0,"}":0,",":1,"*":2}

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        token=[]
        tmp = ""
        tset = set({"{","}",","})
        n = len(expression)
        for i,a in enumerate(expression):
            if a in tset:
                if a =="{" and i>0 and expression[i-1] != "," and expression[i-1] !="{" :
                    if len(tmp) !=0:
                        token.append(tmp)
                        tmp = ""
                    token.append("*")
                
                if len(tmp) !=0:
                    token.append(tmp)
                    tmp = ""
                token.append(a)
                if a =="}" and i <n-1 and expression[i+1] != "," and expression[i+1] != "{" and expression[i+1] != "}"  and token[-1] != "*":
                    token.append("*")
            else:
                tmp = tmp +a
            #print(tmp)
        if len(tmp) !=0:
            token.append(tmp)
            tmp = ""
        #print(token)
        re = midToPost(token,ordDic)
        #print(re)
        st = []
        for a in re:
            if a ==",":
                a1 = st.pop()
                a2 = st.pop()
                a1.extend(a2)
                st.append(a1)
            elif a =="*":
                a1 = st.pop()
                a2 = st.pop()
                res = []
                for a in a2:
                    for b in a1:
                        res.append(a+b)
                res = set(res)
                st.append(list(res))
            else:
                st.append([a])
        re =st[0]
        re = list(set(re))
        re.sort()
        return re
        
                

re = Solution().braceExpansionII("{a,b}{c,{d,e}}") 
re = Solution().braceExpansionII("{a,b}c{d,e}f") 
print(re)
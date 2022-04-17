def midToPost(arr,ordDic):
    res =[]
    st =[]
    for a in arr:
        if a not in ordDic:
            res.append(a)
        else:
            if a =="(":
                st.append(a)
            elif a == ")":
                while st and st[-1] !="(":
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

arr = ["(","12" ,"+","53", ")" , "*","(" ,"10","*","20","+","3","*","2",")"]
ordDic = {"(":0,")":0,"+":1,"*":2}
re = midToPost(arr,ordDic)
print(re)
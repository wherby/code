# ./pic/infixToSuffix.png
def infixTosurffix(ls):
    ord = {"+":1,"-":1,"*":2,"/":2,"++":-100,"(":0,"+++":-99}
    ls.append("+++")
    res = []
    st =["++"]
    n = len(ls)
    idx =0
    while idx <n:
        a = ls[idx]
        print(a)
        if a.isdigit():
            res.append(a)
        else:
           
            if a =="(":
                st.append(a)
            elif a ==")":
                while idx <n and st[-1] != "(":
                    res.append(st.pop())
                st.pop()
            else:
                while ord[st[-1]] >= ord[a]:
                    res.append(st.pop())
                st.append(a)
        idx +=1
        print(res,st)







ls =["(","14","+","3","*","(" ,"1","+","7",")",")","/","2","-","3"]
infixTosurffix(ls)
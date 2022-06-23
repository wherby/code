def testStream(inStr):
    n = len(inStr)
    ls = [0]*26
    st= []
    res = ["#"]*n
    for i,a in enumerate(inStr):
        k = ord(a)-ord('a')
        if ls[k] ==0:
            ls[k] =1
            st.append(a)
        elif ls[k] ==1:
            ls[k]=2
        while st and ls[ord(st[0])-ord('a')] ==2:
            st.pop(0)
        if st:
            res[i] = st[0]
    print(res)
    return res

testStream("google")
testStream("abcdef")
#verified  https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
def monoStack(ls):
    ls.append(0)
    n = len(ls)
    st =[-1]
    ans =0
    for i in range(n):
        a = ls[i]
        while st and ls[st[-1]] >a:
            k = st.pop()
            #print(k,i,ls[k],st)
            ans = max(ans,(i-st[-1]-1)*ls[k]) # st[-1] is record the boundary index which less than ls[k]  
        st.append(i)
    return ans







ls = [2,1,3,4,2,3,3,5,6]
print(monoStack(ls))
# pic/minimumAlpha.png
def minimumAlpha(st1):
    n = len(st1)
    st1 = st1 +st1
    i,j=0,1
    while i <n and j <n:
        k =0
        while k<n and st1[i+k] ==st1[j+k]:
            k +=1
        if k == n:
            break
        if st1[i+k]> st1[j+k]:
            i = i +k+1
            if i==j: i+=1
        else:
            j = j +k +1
            if i==j : j +=1
    ans = min(i,j)
    return st1[ans:ans +n]

st1 = "bacdaa"
re = minimumAlpha(st1)
print(re)
st1 = "daacdaa"
re = minimumAlpha(st1)
print(re)
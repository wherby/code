#check if string a is sub string b in O(n) time
# 
# 

def check(stra,strb):
    m = len(stra)
    n = len(strb)
    idx =0
    for i in range(n):
        if idx <m and strb[i] == stra[idx]:
            idx +=1
    return idx == m

stra = "abcd"
strb = "xyaxbbcyde"
print(check(stra,strb))
stra = "abcd"
strb = "xyaxbbcye"
print(check(stra,strb))
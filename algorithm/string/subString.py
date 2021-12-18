#check if string a is sub string b in O(n) time
# 
# 如果求 a,b的最大公共字符串是lcs

# check if stra is substring of strb => strb 包含stra的所有顺序字符
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
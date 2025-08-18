


def baseLine(s1):
    n = len(s1)+1
    ls = [1]*n 
    mn = 0
    for i,a in enumerate(s1):
        if a == "L":
            ls[i+1] = ls[i] -1 
        elif a =="R":
            ls[i+1] = ls[i] +1 
        else:
            ls[i+1] = ls[i]
        mn = max(mn,1-ls[i+1])
    if mn:
        ls = [a + mn for a in ls]
    return ls


s1 = "LRLR"
print(baseLine(s1))
s2 = "=RRRLL"
print(baseLine(s2))
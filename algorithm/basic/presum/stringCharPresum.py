
def getPre(s):
    pre = [[0 for _ in range(26)]]
    for a in s:
        pre.append(list(pre[-1]))
        pre[-1][ord(a)- ord('a')] +=1
    return pre

s ="abbacdeaa"
print(getPre(s))
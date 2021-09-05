
def generate(ls,ran):
    res = []
    for x in ran:
        for y in ls:
            t = list(y)
            t.append(x)
            res.append(t)
    return res

def getlen(ls,subls):
    n = len(subls)
    cnt = 0
    for i in range(n):
        if ls[i] != subls[i]:
            return cnt
        cnt = cnt +1
    return cnt

def getMaxLen(ls):
    n = len(ls)
    MX =0
    for i in range(1,n):
        if ls[i] == ls[0]:
            tpmx = getlen(ls,ls[i:])
            if tpmx >MX:
                MX = tpmx
    return MX

ls = [[1]]
ran = [1,2]
sumls =[]
for cc in range(1,6):
    ls = [[1]]
    ran = [1,2]
    for i in range(cc):
        ls = generate(ls,ran)
    lenls =[getMaxLen(x) for x in ls]
    sumls.append(sum(lenls))
    print  len(lenls),sum(lenls)
print sumls
# n = len(sumls)
# resls =[]
# for i in range(n-1,0,-1):
#     res = sumls[i] - sumls[i-1] *4
#     print res
#     resls.append(res)
# for i in range(n-2):
#     ress = resls[i] -resls[i+1] *3
#     print ress
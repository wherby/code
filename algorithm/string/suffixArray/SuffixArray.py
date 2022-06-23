# file:///C:/Users/where/software/e-maxx-eng/public/string/suffix-array.html


from math import ceil, log

# sort lenght =1
def sortFirst(strA):
    n = len(strA)
    Alphabet = 256
    p,c,cnt = [0]*n, [0]*n,[0]*Alphabet
    for i in range(n):
        cnt[ord(strA[i])] +=1
    for i in range(1,Alphabet):
        cnt[i] += cnt[i-1]
    for i in range(n-1,-1,-1):
        cnt[ord(strA[i])] =cnt[ord(strA[i])] -1
        t =cnt[ord(strA[i])]
        p[t] = i 
    c[p[0]] =0
    classes = 1
    for i in range(1,n):
        if strA[p[i]] != strA[p[i-1]]:
            classes +=1
        c[p[i]] = classes -1
    #print(p,c)
    return (p,c)

def SuffixArraySort(strA):
    n = len(strA)
    Alphabet = 256
    p,c = sortFirst(strA)
    pn,cn,cnt =[0]*n ,[0]*n,[0]*(max(Alphabet,n))
    for h in range(int(log(n-1,2))+1):
        for i in range(n):
            pn[i] =p[i]-(1<<h)
            if pn[i] < 0:
                pn[i] +=n 
        cnt = [0]*n
        for i in range(n):
            cnt[c[pn[i]]] +=1
        for i in range(1,n):
            cnt[i] += cnt[i-1]
        for i in range(n-1,-1,-1):
            cnt[c[pn[i]]]=cnt[c[pn[i]]] -1
            t = cnt[c[pn[i]]]
            p[t] =pn[i]
        cn[p[0]]  =0
        classes =1
        for i in range(1,n):
            cur = (c[p[i]],c[(p[i] + (1<<h))%n])
            prev = (c[p[i-1]],c[(p[i-1] + (1<<h))%n])
            if cur != prev:
                classes +=1
            cn[p[i]] = classes -1
        c,cn = cn,c
        #print(c,p)
    #print(cn,pn,p)
    return p

# return the sorted list of prfix array
## ret =[3,0,1,2]
## means the fist one in sorted prefix array is arr[3:] 
## and the sorted prefix array is [arr[3:],arr[0:],arr[1:],arr[2:]]    
def getSortedArrayList(strA):
    strA +="$"
    ret = SuffixArraySort(strA)
    #print(ret)
    ret =ret[1:]
    return ret
    
def getOrd(ret):
    n = len(ret)
    res = [0]*n
    for i,a in enumerate(ret):
        res[a] =i
    return res

s1 = "aaabacdbac"
s2 = "abaab"
s3 ="abaab$"
re =SuffixArraySort(s3)
print(re)
re2 = getSortedArrayList(s2)
print(re2)
s3 ="aaaaaaaaaaaaab"
print(getSortedArrayList(s3))
s4 = "aaaaaabaaaaaaaaaaa"
print(getSortedArrayList(s4))
print("real order")
print(getOrd(getSortedArrayList(s4)))
# s5 = "aaaaaaaaaaaaaaaaaa"
# print(getSortedArrayList(s5))
# s4 = "aaaaaabaaaaaa"
# sortFirst(s4)
# print(getSortedArrayList(s4))
s5= "aaba"
SuffixArraySort(s5)
print(getSortedArrayList(s5)) 
#https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/


##cmpStruct is not used for default compare in python is the same 
def cmpStruct(a,b):
    if a[1] == b[1]:
        return [1,-1][a[2]<b[2]]
    else:
        return [1,-1][a[1]<b[1]]

def getNumFromChar(a):
    return ord(a) -ord('a')

def buildSuffixArray(txt):
    n = len(txt)
    suffixes = []
    for i in range(n):
        tp = [i, getNumFromChar(txt[i]),getNumFromChar(txt[i+1]) if i+1 <n else -1]
        suffixes.append(tp)
    suffixes = sorted(suffixes,cmp=cmpStruct)
    #print suffixes
    ind = [0]*n
    k= 4
    while k< 2*n:
        rank =0
        prev_rank =suffixes[0][1]
        suffixes[0][1] = rank
        ind[suffixes[0][0]] = 0
        for i in range(1,n):
            if suffixes[i][1] ==prev_rank and suffixes[i][2] == suffixes[i-1][2]:
                prev_rank = suffixes[i][1]
                suffixes[i][1] = rank
            else:
                prev_rank = suffixes[i][1]
                rank = rank +1
                suffixes[i][1] = rank
            ind[suffixes[i][0]] =i

        for i in range(n):
            nextindex = suffixes[i][0] + k/2
            suffixes[i][2] = suffixes[ind[nextindex]][1] if nextindex <n else -1
        suffixes = sorted(suffixes,cmp=cmpStruct)
        k=k*2
    suffixindex = []
    for i in range(n):
        suffixindex.append(suffixes[i][0])
    return suffixindex




txt = "abbababba"
print buildSuffixArray(txt) 
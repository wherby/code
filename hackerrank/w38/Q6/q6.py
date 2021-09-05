filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import bisect

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)



n, = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())

vls =[0]
for x in ls:
    vls.append(x)

relat =[]
for i in range(n +1):
    relat.append([])
index = 2
for i in range(n-1):
    a,b, = map(int , ins[index +i].strip().split())
    relat[a].append(b)
    relat[b].append(a)



def searchSeg(segs):
    global relat,vls,searchResult
    u=segs[0][1]
    segList =[]
    for seg in segs:
        segList.append(seg[2])
    dic1 ={u:1}
    visiting = [u]
    res =[u]
    d =0
    result = [vls[u]]
    index =0
    while d<=segList[-1]:
        while index < len(segs) and segs[index][2] == d :
            k = segs[index][3]
            if k <=len(result):
                tmp =result[k-1]
            else:
                tmp= -1 
            searchResult[segs[index][0]] =tmp
            #print tmp ,segs[index],result,k
            index = index +1
        tmp=[]
        for i in visiting:
            for j in relat[i]:
                if j not in dic1:
                    dic1[j] =1
                    res.append(j)
                    tmp.append(j)
                    result.append(vls[j])#bisect.insort_left(result, vls[j])
        d  = d +1
        visiting = tmp  


q, = map(int , ins[n+1].strip().split())
index = n +2
searchOrder = []
for i in range(q):
    u,d,k, = map(int , ins[index +i].strip().split())
    searchOrder.append([i,u,d,k])
searchOrder= sorted(sorted(searchOrder, key = lambda x : x[2]), key = lambda x : x[1])

segSearch = []
k = searchOrder[0][1]
res =[]
searchResult = [0]*q
for temp in searchOrder:
    if temp[1] == k:
        res.append(temp)
    else:
        segSearch.append(res)
        k =temp[1]
        res= [temp]
segSearch.append(res)
#print segSearch
for segs in segSearch:
    searchSeg(segs)

for i in searchResult:
    print i

print searchOrder
print searchResult
#print vls,relat

from typing import List, Tuple, Optional
# common include
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from sortedcontainers import SortedDict,SortedList
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter
from functools import lru_cache
from functools import cache



def toTree(ls):
    ls.append(None)

    acc =0
    for i,a in enumerate(ls):
        if a != None:
            
            acc +=1
            ls[i] = str(acc) + "@" + str(a)
    #print(ls)
    
    dic = defaultdict(list)
    tls = []
    tm= []
    for a in ls:
        if a != None:
            tm.append(a)
        else:
            tls.append(tm)
            tm =[]
    n=len(tls)
    cur = 1
    cand =tls[0]
    while cand:
        tmp =[]
        for a in cand:
            
            if cur < n:
                dic[a] =tls[cur]
                tmp.extend(tls[cur])
                cur +=1
            #print(a,tls[cur],dic,tmp)
        cand = tmp
    #print(dic)

    res =[]
    def dfs(root):
        if root!= None:
            res.append(root)
            for a in dic[root]:
                dfs(a)
    dfs(ls[0])
    for i,a in enumerate(res):
        idx =a.find("@")
        res[i] = a[idx+1:]
    if len(res) != acc :
        return "Invalid  input"
    return res


ls1 =[1,None,1,2,4,None,5,1]
ls3= [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
ls2= [1,None,2,3,4,None,None,None,None,5,6,7,None,None,None,8,None,None,None]
ls4 = ["1",None, ]

ls5 = [1,2,3,4,5,None]
ls6 =[None,1,2,4]
ls7=["a",None,"b","c"]
#ls1=  toTree(ls)
#print(ls1)


lss = [ls1,ls2,ls3,ls4,ls5,ls6,ls7]
for a in lss:
    print(toTree(a))

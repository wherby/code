
from bisect import bisect_right,insort_left,bisect_left
def dfs(idx, mn,lss):
    if idx == 0:
        return lss
    if mn ==True:
        lss.extend([ls[-1] for _ in range(idx)] )
        return lss
    else:
        k= bisect_right(ls,num[idx-1])
        if k == 0 :
            return dfs(idx-1,True,lss)
        elif num[idx-1] == ls[k-1]:
            lss.append(ls[k-1])
            return dfs(idx-1,False,lss)
        else:
            lss.append(ls[k-1])
            return dfs(idx-1,True,lss)

ls =[1,2,9,4]
ls.sort()
num = 2533
num = [int(a) for a in str(num)]
num = num[::-1]

re =dfs(len(num),False,[])
print(re)
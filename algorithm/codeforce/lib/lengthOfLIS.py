# LIS Longest increase sequence
from bisect import bisect_right,insort_left,bisect_left
def lengthOfLIS(ls):
    ans = []
    for x in ls:
        if not ans or ans[-1]<x:
            ans.append(x)
        else:
            i = bisect_left(ans,x)
            ans[i] = x 
        #print(ans,x)
    return len(ans)
if __name__ =="__main__":
    ls = [1,4,2,3,5,11,9,7,8,12]
    print(lengthOfLIS(ls))
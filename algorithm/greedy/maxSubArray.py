
def findMax(nums,start):
    ans = -10**10
    min_pre,pre_sum = 0,0
    s1 = start
    ret =[s1,s1]
    for i,a in enumerate(nums,start):
        pre_sum += a 
        if ans <pre_sum-min_pre:
            ans = pre_sum-min_pre
            ret = [s1,i+1]
        if min_pre > pre_sum:
            min_pre =pre_sum
            s1=i+1
    #print(nums,start,ret,s1,pre_sum,min_pre)
    return ret

ls= [3,-87,21,-86,44,-36,80]
st,end = findMax(ls,0)
print(st,end,sum(ls[st:end]))
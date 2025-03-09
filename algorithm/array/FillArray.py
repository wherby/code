# 填充得到最大值
def fillFunc(ls, offer):
    ls.sort()
    n = len(ls)
    pre_sum= j =0
    while j < n and ls[j]*j <= pre_sum + offer:
        pre_sum += ls[j]
        j+=1
    return (pre_sum + offer) //j
    

ls = [1,1,2,2,3,4,5,6,7]

for i in range(30):
    print(fillFunc(ls,i),i)
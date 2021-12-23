cnt =0

def allCombination(idx):
    global cnt
    if idx ==n :
        cnt +=1
        print(res)
        return
    allCombination(idx+1)
    res.append(arr[idx])
    allCombination(idx+1)
    res.pop()

arr = [1,2,3,4,5,6,7]
n = len(arr)
res =[]


allCombination(0)
print(cnt)
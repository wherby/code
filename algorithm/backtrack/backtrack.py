# pic/backtrack.png
cnt =0

def allCombination(idx):
    global cnt
    if idx ==n :
        cnt +=1
        print(res)
        return
    allCombination(idx+1) # without idx
    res.append(arr[idx])  # add idx
    allCombination(idx+1) # with idx
    res.pop()             # recover back

arr = [1,2,3,4,5,6,7]
n = len(arr)
res =[]


allCombination(0)
print(cnt)
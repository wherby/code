# pic/reversePair.png
cnt =0
def merge(l,mid,r):
    global cnt
    # merge a[l,mid] and a[mid+1, r]
    i,j = l ,mid +1
    for k in range(l,r+1):
        if j>r or (i <= mid and a[i] <=a[j]):
            b[k] = a[i]
            i +=1
        else:
            b[k] = a[j]
            j+=1
            cnt = cnt + mid -i +1
    for k in range(l,r+1):
        a[k] = b[k]

def mergeSort(l,r):
    if l == r:
        return
    mid = (l+r) //2
    mergeSort(l,mid)
    mergeSort(mid+1,r)
    merge(l,mid,r)


a = [5,6,7,8,1,2,3,4]
b = [0]*8
merge(0,3,7)
print(b,cnt)

cnt =0
a = [8,7,6,5,4,3,2,1]
#a = [1,2,3,4,5,6,7,8]
b = [0]*8
mergeSort(0,7)
print(b,cnt)


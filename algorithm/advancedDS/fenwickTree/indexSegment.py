# ./pic/indexSeg.png
# for 1-index array
def seg(x):
    while x>0:
        print(x-(x&-x)+1,x)
        x-=x&-x

seg(13)
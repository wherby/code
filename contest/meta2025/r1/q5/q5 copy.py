

from collections import defaultdict,deque
def resolve():
    N, = list(map(lambda x: int(x),input().split()))
    ls =list(map(lambda x: int(x),input().split()))
    dic = defaultdict(int)
    dic[0]=1
    cur = 0  
    acc =0
    ret =0
    for i,a in enumerate(ls):
        cur = (i+1)*(i+2) //2
        #print(cur,i)
        acc =acc ^ a 
        ret +=cur - dic[acc]*(dic[acc]+1)//2
        dic[acc]+=1
        
        
    return ret

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)
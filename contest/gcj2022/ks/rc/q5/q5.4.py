import random
def resolve():
    i1 = list(map(lambda x: int(x),input().split()))
    n,k = i1[0],i1[1]
    ls = [-1]*(n+1)
    i1 = list(map(lambda x: int(x),input().split()))
    tls = [i for i in range(1,n+1)]
    random.shuffle(tls)
    random.shuffle(tls)
    a,b = i1[0],i1[1]
    ls[a] = b
    cnt = 0
    visited =1
    sm = b
    isMeet =False
    start =0
    while cnt < k :        
        a1 = a
        b1 = b
        print("W")
        i1 = list(map(lambda x: int(x),input().split()))
        a,b = i1[0],i1[1]
        if ls[a] != -1:
            isMeet =True
            sm += b 
            visited +=1
            sm += (b1)*b 
            visited += (b)
            visited += (b1)
        else:
            sm += b 
            visited +=1
            sm += (b1)*b 
            visited += (b)
            visited += (b1)
            ls[a] =b
        cnt +=1
        if (isMeet) and cnt<k :
            for i in range(start,n):
                if ls[tls[i]] == -1:
                    start =i+1
                    break
            print("T " + str(tls[i]))
            i1 = list(map(lambda x: int(x),input().split()))
            a,b = i1[0],i1[1]
            sm += b
            visited +=1
            ls[a] =b
            cnt +=1
    guess = int(sm /visited *n)
    print("E "+str(guess))
    
def op(caseidx):
    resolve()
    

for i in range(int(input())):
    op(i)
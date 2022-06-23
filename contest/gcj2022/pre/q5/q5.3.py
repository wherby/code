import random
import heapq
def resolve():
    i1 = list(map(lambda x: int(x),input().split()))
    n,k = i1[0],i1[1]
    ls = [-1]*(n+1)
    i1 = list(map(lambda x: int(x),input().split()))
    tls = [i for i in range(1,n+1)]
    random.shuffle(tls)
    g = [[] for _ in range(n+1)]
    a,b = i1[0],i1[1]
    ls[a] = b
    cnt = 0
    start =0
    st =[]
    visited =0
    sm = 0
    acc =0
    while cnt < k :
        if st and cnt+2  <k:
            a = st.pop()
            print("T " + str(a))
            i1 = list(map(lambda x: int(x),input().split()))
            print("W")
            i1 = list(map(lambda x: int(x),input().split()))
            a,b = i1[0],i1[1]
            sm += b
            visited +=1
            ls[a] =b
            g[a1].append(a)
            g[a].append(a1)
            if len(g[a1]) <int(b1 * k/n):
                st.append(a1)
            if len(g[a]) <int(b* k/n):
                st.append(a)
            cnt +=2
        else:
            if acc > int( n//k *2):
                acc -=int( n//k *2)
                a1 = a
                b1 = b
                print("W")
                i1 = list(map(lambda x: int(x),input().split()))
                a,b = i1[0],i1[1]
                sm += b
                visited +=1
                ls[a] =b
                g[a1].append(a)
                g[a].append(a1)
                if len(g[a1]) <int(b1 * k/n):
                    st.append(a1)
                if len(g[a]) <int(b* k/n):
                    st.append(a)
            else:
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
                acc +=b
            cnt +=1
    guess =int((sm * n /(visited *2) ))
    print("E "+str(guess))
    
def op(caseidx):
    resolve()
    

for i in range(int(input())):
    op(i)
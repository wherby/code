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
            if len(g[a1]) <b1-2:
                st.append(a1)
            if len(g[a]) <b-2:
                st.append(a)
            cnt +=2
        else:
            if (len(g[a]) < b)  :
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
                if len(g[a1]) <b1:
                    st.append(a1)
                if len(g[a]) <b:
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
            cnt +=1
    guess =int((sm * n /(visited *2) ))
    print("E "+str(guess))
    
def op(caseidx):
    resolve()
    

for i in range(int(input())):
    op(i)
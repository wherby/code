N = 10
ls = [i for i in range(N)]
ls = ls[::-1]
cnt = 0
vs = []
st =set()
for total in range(2*N-1):
    for i in range(max(total-N+1,0),N):
        u  = ls[i]
        v = ls[total - i]
        #print(u,v)
        if total -i >=0:
            vs.append((u,v,total,total -i))
            st.add((u,v))
            cnt +=1
print(cnt)
print(vs)
print(len(st))
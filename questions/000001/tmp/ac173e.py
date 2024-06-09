# https://atcoder.jp/contests/arc173/tasks/arc173_e

#N=int(input());A=[a|1<<62 for a in map(int,input().split())];ans=0;T=[]
N= 13
st="451745518671773958 43800508384422957 153019271028231120 577708532586013562 133532134450358663 619750463276496276 615201966367277237 943395749975730789 813856754125382728 705285621476908966 912241698686715427 951219919930656543 124032597374298654"
A=[a|1<<62 for a in map(int,st.split())];ans=0;T=[]
#print(A)
for x in A:
 y=x
 for j,b in enumerate(T):y=min(y,y^b)
 if y:T=[min(t,t^y)for t in T]+[y]
 #print(T)
#print(T)
T.sort();b=T.pop()^1<<62;y=0
for x in T[::-1]:y=max(y,y^x)
if N%4==2:
 a=0
 for i in range(N):a^=A[i]
 if a==y and len(T)==N-1:y^=T[0]
if N==2:
 y=A[0]^A[1]
print(y)
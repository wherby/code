
ls =[]
N= 12
for i in range(N):
    ls.append(1<<i)
#ls= ls[5:]+ls[:5]

for i in range(N-1):
    tmp =[]
    for j in range(N-i-1):
        tmp.append(ls[j]^ls[j+1])
    ls= tmp 
print(bin(ls[0]))
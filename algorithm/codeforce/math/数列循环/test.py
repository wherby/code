
p = [4,3,1,2]
p =[a-1 for a in p]

cur = list(range(4))
for i in range(4):
    cur = [p[i] for i in cur]
    print(cur)

q = [0]*4 
for i in range(4):
    q[p[i]] = i 

for i in range(4):
    cur = [q[i] for i in cur ]
    print(cur)
print("a")
cur = list(range(4))
for i in range(4):
    cur = [q[i] for i in cur ]
    print(cur)

for i in range(4):
    cur = [p[i] for i in cur]
    print(cur)

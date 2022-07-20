
def resolve():
    inp = int(input())
    x= min(30,inp)
    seed1 = [1<<i for i in range(0,x)]
    seedLeft =[]
    for b in range(x,inp):
        seedLeft.append(2**10 +b+1)
    seed = seed1 +seedLeft
    ts =[str(x) for x in seed]
    ts= " ".join(ts)
    print(ts)
    ls2 = list(map(lambda x: int(x),input().split()))
    allls = seed +ls2
    sm = sum(allls)
    hf = sm //2
    remains = hf
    res =[]
    left, right =0,0
    ls2 = ls2 + seedLeft
    ls2.sort(reverse= True)
    for i in range(len(ls2)//2):
        if left> right:
            left += ls2[i*2 +1]
            right += ls2[i*2]
            res.append(ls2[i*2 +1])
        else:
            left += ls2[i*2 ]
            right += ls2[i*2+1]
            res.append(ls2[i*2 ])
    remains -= left
    seed1.sort(reverse= True)
    for a in seed1:
        if remains >=a:
            res.append(a)
            remains -=a
    ts =[str(x) for x in res]
    ts= " ".join(ts)
    print(ts)
def op(caseidx):
    resolve()

for i in range(int(input())):
    op(i)
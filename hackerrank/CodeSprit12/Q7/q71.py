def S(ls):
    n = len(ls)
    for k in range(n):
        for i in range(n-k):
            j =i+k
            print i,j


ls =[0]*10
S(ls)
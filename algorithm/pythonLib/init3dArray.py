arr = [[[0]*10 for _ in range(10) ] for _ in range(10)]
for i in range(10):
    for j in range(10):
        for k in range(10):
            arr[i][j][k] = i*100+j*10 +k
print(arr)
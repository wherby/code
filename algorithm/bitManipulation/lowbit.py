def lowbit(n):
    return n &(-n+1)

print(lowbit(12))
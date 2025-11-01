
n=32

notes = [''.join(str(i >> j & 1) for i in range(n)) for j in range(5)]
print(notes)
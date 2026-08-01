# https://wherby.github.io/code/algebra/gray-code.html

## binary to Gray
def grayCode(n):
    return n^(n>>1)

for i in range(16):
    print(i, " to  Gray is", grayCode(i))


# Gray to binary:

def reverseGray(g):
    n = 0
    while g:
        n = g ^n 
        g = g >>1
    return n 

for i in range(16):
    print(i , " gray to index: ", reverseGray(i))

for i in range(16):
    print(i, reverseGray(grayCode(i)))

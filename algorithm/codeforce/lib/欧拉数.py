

def getPhi(M):
    phi = list(range(M + 1))
    for i in range(2, M + 1):
        if phi[i] == i:
            for j in range(i, M + 1, i):
                phi[j] -= phi[j] // i
    return phi


if __name__ == '__main__':
    phi = getPhi(100)
    print(phi)


def main(n):
    n = n
    ans = [0] * (2 * n)

    for i in range(n):
        ans[i] = i + 1

    for i in range(n):
        cur = 0
        for j in range(0, n, i + 1):
            ans[i + j], cur = cur, ans[i + j]
        ans[i + n] = cur
        print(i,ans)

    print(' '.join(map(str, ans[n:])))

main(10)
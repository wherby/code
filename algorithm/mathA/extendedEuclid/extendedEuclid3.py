

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad13d
# https://brilliant.org/wiki/extended-euclidean-algorithm/
# https://cp-algorithms.com/algebra/extended-euclid-algorithm.html
# 一样的功能，先假设欧几里德算法得到一个x==1,y ==0的时候的值，为最小功倍数，然后求出化简之前的x,y
# int gcd(int a, int b, int& x, int& y) {
#     if (b == 0) {
#         x = 1;
#         y = 0;
#         return a;
#     }
#     int x1, y1;
#     int d = gcd(b, a % b, x1, y1);
#     x = y1;
#     y = x1 - y1 * (a / b);
#     return d;
# }


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

print(egcd(1432,123211))
gcd,x,y =egcd(1432,123211)
d = 1432*x + 123211*y
print(d)
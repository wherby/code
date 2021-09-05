####Problem Setter's code :
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <algorithm>
#include <stack>
#include <cassert>
#include <map>
#include <set>
#include <deque>
#include <complex>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
const long long MOD = 1e9 + 7;
long long a[1<<16];
long long INV2;

long long modpow(long long a, long long b) {
    if(b == 0) return 1;
    if(b == 1) return a;
    if(b&1LL) return (a * modpow(a,b-1LL)) % MOD;
    long long k = modpow(a,b/2LL);
    return (k*k)%MOD;
}

void transform(int x, int y) {
    if(x == y - 1) {
        return;
    }
    int l2 = (y-x)/2;
    int z = x + l2;
    transform(x,z);
    transform(z,y);
    for(int i = x;i<z;i++) {
        int x1 = a[i];
        int x2 = a[i+l2];
        a[i] = (x1 - x2 + MOD) % MOD;
        a[i+l2] = (x1 + x2) % MOD;
    }
}

void untransform(int x, int y) {
    if(x == y - 1) {
        return;
    }
    int l2 = (y-x)/2;
    int z = x + l2;
    for(int i = x;i<z;i++) {
        long long y1 = a[i];
        long long y2 = a[i+l2];
        a[i] = (int) (((y1 + y2) * INV2) % MOD);
        a[i+l2] = (int) (((y2 - y1 + MOD) * INV2) % MOD);
    }
    untransform(x,z);
    untransform(z,y);
}

int n, v, t;

int arr[100005];

int main() {
    INV2 = modpow(2, MOD - 2LL);
    t = 1<<16;

    scanf("%d", &n);
    assert(n > 0 && n <= 100000);

    for(int i = 1;i<=n;i++) {
        scanf("%d", &arr[i]);
        assert(arr[i] >= 0 && arr[i] < 65536);

        arr[i] ^= arr[i-1];
        ++a[ arr[i] ];
    }

    transform(0,t);

    for(int i = 0;i<t;i++) {
        a[i] = (a[i] * a[i]) % MOD;
    }

    untransform(0,t);

    a[0] -= (long long) n;

    for(int i = 0;i<t;i++) {
        a[i] /= 2LL;
    }

    for(int i = 1;i<=n;i++) {
        ++a[ arr[i] ];
    }

    int sol = 0;
    long long maxx = 0;

    for(int i = 0;i<t;i++) {
        if(a[i] > maxx) {
            maxx = a[i];
            sol = i;
        }
    }

    printf("%d %lld\n", sol, maxx);

    return 0;
}
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <unordered_map>
using namespace std;

const long long dv = 1000000007;

long long gcd(long long a, long long b) {
    while (b) {
        long long m = a % b;
        a = b;
        b = m;
    }
    return a;
}

long long reduce(vector<long long> &v) {
    long long g = 0;
    for (long long x: v) {
        g = gcd(g, x);
    }
    for (long long &x: v) {
        x /= g;
    }
    return g;
}

string key(const vector<long long>& v, long long g) {
    string result;
    for (int x : v) {
        result += (to_string(x) + " ");
    }
    result += to_string(g);
    return result;
}


long long pw(long long x, long long n) {
    long long res = 1;
    while (n > 0) {
        if (n & 1) res = (res * x) % dv;
        x = (x * x) % dv;
        n >>= 1;
    }
    return res;
}

int main() {
    int n, x, s, f, m;
    cin >> n >> x >> s >> f >> m;
    int a[n][n];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    
    
    
    vector<long long> v(n);
           
    unordered_map<string, int> keys;
    vector<vector<long long>> vv(2);
    vv[1].resize(n);
    for (int i = 0; i < n; i++) {
        vv[1][i] = a[s][i];        
    }
    
    vector<long long> fin;
    vector<long long> gg(2);
    
    
    long long int dd = x;    
    for (int w = 2; w <= m; w++) {
        vv.resize(w + 1); gg.resize(w + 1);
        vv[w].resize(n, 0);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                vv[w][i] = max(vv[w][i], vv[w-1][j] * a[j][i]);
            }
        }        
        gg[w] = reduce(vv[w]);
        
        string k = key(vv[w], gg[w]);        
        if (keys.find(k) != keys.end()) {
            int p = keys[k];
            
            int l = w - p;
            long long togo = m - w;

            fin = vv[p + togo % l];
            for (int i = p; i < w; i++) {
                dd = (dd * pw(gg[i], togo / l + ((i - p) <= togo % l))) % dv;
            }
            break;
        }
        
        keys[k] = w;
        dd = (dd * gg[w]) % dv;                
        if (w == m) {
            fin = vv[w];
        }        
    }
    cout << (fin[f] * dd) % dv << endl;
    return 0;
}
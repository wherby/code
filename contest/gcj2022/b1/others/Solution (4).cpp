#include <bits/stdc++.h>

using namespace std;

mt19937 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

constexpr int N = 8;
constexpr int M = 256;

typedef bitset<M> Set;
int bits[M];
Set who[N + 1];
Set to[M][M];

int rotate(int x, int r) {
    int l = 8 - r;
    int y = x & ( (1 << r) - 1 );
    return (x >> r) | (y << l);
}

void pre() {
    for(int i = 0; i < M; i++) {
        for(int j = 0; j < N; j++)
            if( (i >> j) & 1 )
                bits[i]++;
        who[ bits[i] ][i] = 1;
    }

    for(int i = 0; i < M; i++)
        for(int j = 0; j < M; j++) {
            for(int r = 0; r < N; r++)
                to[i][j][i ^ rotate(j, r)] = 1;
        }
}

int query(int x) {
    string s;
    for(int i = 0; i < N; i++)
        s.push_back('0' + ((x >> i) & 1));
    reverse(begin(s), end(s));
    cout << s << endl;

    int ans;
    cin >> ans;
    if(ans == -1)   exit(0);
    return ans;
}

void solve_test() {
    int k = query(0);
    Set can = who[k];

    const int BULAN = 16;
    while(k > 0) {
        int best = M + 1;
        int best_val = -1;
        Set best_next_can;

        if(can.count() <= BULAN) {
            vector<int> options;
            for(int i = 0; i < M; i++)
                if(can[i])  options.push_back(i);
            shuffle(begin(options), end(options), rng);

            best_val = options[0];
            for(auto x: options)
                best_next_can |= to[x][best_val];
        } else {

            for (int v = 1; v < M - 1; v++) {
                Set next_can;
                for (int i = 0; i < M; i++)
                    if (can[i])
                        next_can |= to[i][v];

                if (next_can.count() < best) {
                    best = next_can.count();
                    best_val = v;
                    best_next_can = next_can;
                }
            }
        }

        k = query(best_val);
        can = best_next_can & who[k];
    }
}

int main() {
//    freopen("1.in", "r", stdin);
    //freopen("1.out", "w", stdout);

    pre();

    int T = 1;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        //printf("Case #%d: ", t);
        solve_test();
    }

    return 0;
}
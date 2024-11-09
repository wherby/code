//#include <bits/stdc++.h>
#include<iostream>
using namespace std;
using i64 = long long;
using u64 = unsigned long long;
using u32 = unsigned;

constexpr int N = 800;

int fen[N][N];

void add(int x, int y, int v) {
    for (int i = x + 1; i <= N; i += i & -i) {
        for (int j = y + 1; j <= N; j += j & -j) {
            fen[i - 1][j - 1] += v;
        }
    }
}

int sum(int x, int y) {
    int res = 0;
    for (int i = x; i; i &= i - 1) {
        for (int j = y; j; j &= j - 1) {
            res += fen[i - 1][j - 1];
        }
    }
    return res;
}

void solve() {
    int R, C;
    i64 K;
    std::cin >> R >> C >> K;
    
    std::vector B(R, std::vector<int>(C));
    std::vector<std::vector<std::array<int, 2>>> f(R * C);
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            std::cin >> B[i][j];
            B[i][j]--;
            f[B[i][j]].push_back({i, j});
        }
    }
    
    auto check = [&](int d) {
        i64 ans = 0;
        for (int b = 0; b < R * C; b++) {
            if (f[b].empty()) {
                continue;
            }
            for (auto [x, y] : f[b]) {
                add(x, y, 1);
            }
            for (auto [x, y] : f[b]) {
                int lx = std::max(0, x - d);
                int rx = std::min(R, x + 1 + d);
                int ly = std::max(0, y - d);
                int ry = std::min(C, y + 1 + d);
                ans += (rx - lx) * (ry - ly);
                ans -= sum(lx, ly);
                ans += sum(lx, ry);
                ans += sum(rx, ly);
                ans -= sum(rx, ry);
            }
            for (auto [x, y] : f[b]) {
                add(x, y, -1);
            }
        }
        return ans;
    };
    
    int lo = 1, hi = std::max(R, C) - 1;
    while (lo < hi) {
        int x = (lo + hi) / 2;
        if (K <= check(x)) {
            hi = x;
        } else {
            lo = x + 1;
        }
    }
    
    std::cout << lo << "\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int T;
    std::cin >> T;
    
    for (int i = 1; i <= T; i++) {
        std::cerr << "Case #" << i << ": ";
        std::cout << "Case #" << i << ": ";
        solve();
    }
    
    return 0;
}

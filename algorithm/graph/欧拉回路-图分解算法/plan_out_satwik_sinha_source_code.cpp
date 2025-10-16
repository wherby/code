#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>

using namespace std;
using ll = long long;

struct DSU {
    int n;
    vector<int> p;
    vector<int> sz;

    explicit DSU(int n = 0) : n(n), p(n), sz(n, 1) {
        iota(p.begin(), p.end(), 0);
    }

    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return;
        if (sz[a] < sz[b]) swap(a, b);
        p[b] = a;
        sz[a] += sz[b];
    }
};

void solve() {
    int T;
    if (!(cin >> T)) return;
    for (int tc = 1; tc <= T; ++tc) {
        int n, m;
        cin >> n >> m;
        vector<int> a(m), b(m);
        for (int i = 0; i < m; i++) {
            cin >> a[i] >> b[i];
            --a[i];
            --b[i];
        }
        vector<int> deg(n, 0);
        DSU dsu(n);
        for (int i = 0; i < m; i++) {
            deg[a[i]]++;
            deg[b[i]]++;
            dsu.unite(a[i], b[i]);
        }
        int S = n;
        vector<vector<int>> adj(n + 1);
        vector<int> eu;
        vector<int> ev;
        vector<int> rid;
        auto add_edge = [&](int u, int v, int id) {
            int idx = static_cast<int>(eu.size());
            eu.push_back(u);
            ev.push_back(v);
            rid.push_back(id);
            adj[u].push_back(idx);
            adj[v].push_back(idx);
        };
        for (int i = 0; i < m; i++) add_edge(a[i], b[i], i);
        for (int v = 0; v < n; v++) {
            if (deg[v] & 1) add_edge(v, S, -1);
        }
        vector<int> rep(n, -1), hasEdge(n, 0), hasOdd(n, 0);
        for (int v = 0; v < n; v++) {
            if (deg[v] > 0) {
                int r = dsu.find(v);
                hasEdge[r] = 1;
                if (rep[r] == -1) rep[r] = v;
                if (deg[v] & 1) hasOdd[r] = 1;
            }
        }
        for (int r = 0; r < n; r++) {
            if (hasEdge[r] && !hasOdd[r]) {
                int v = rep[r];
                add_edge(v, S, -1);
                add_edge(v, S, -1);
            }
        }
        int E = static_cast<int>(eu.size());
        vector<char> used(E, 0);
        vector<int> it(n + 1, 0), stV, stE, res;
        stV.push_back(S);
        while (!stV.empty()) {
            int v = stV.back();
            while (it[v] < static_cast<int>(adj[v].size()) && used[adj[v][it[v]]]) it[v]++;
            if (it[v] == static_cast<int>(adj[v].size())) {
                stV.pop_back();
                if (!stE.empty()) {
                    res.push_back(stE.back());
                    stE.pop_back();
                }
            } else {
                int ei = adj[v][it[v]++];
                if (used[ei]) continue;
                used[ei] = 1;
                int to = eu[ei] ^ ev[ei] ^ v;
                stV.push_back(to);
                stE.push_back(ei);
            }
        }
        vector<int> col(E, 0);
        int cur = 0;
        for (int i = static_cast<int>(res.size()) - 1; i >= 0; i--) {
            col[res[i]] = (cur & 1) ? 2 : 1;
            cur++;
        }
        vector<int> day(m, 1);
        for (int ei = 0; ei < E; ei++) {
            if (rid[ei] >= 0) day[rid[ei]] = col[ei];
        }
        vector<int> d1(n, 0), d2(n, 0);
        for (int i = 0; i < m; i++) {
            int u = a[i], v = b[i];
            if (day[i] == 1) {
                d1[u]++;
                d1[v]++;
            } else {
                d2[u]++;
                d2[v]++;
            }
        }
        ll ans = 0;
        for (int i = 0; i < n; i++) ans += 1LL * d1[i] * d1[i] + 1LL * d2[i] * d2[i];
        string s;
        s.resize(m);
        for (int i = 0; i < m; i++) s[i] = static_cast<char>('0' + day[i]);
        cout << "Case #" << tc << ": " << ans << " " << s << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}

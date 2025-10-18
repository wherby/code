// https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/E?source=facebook

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;
using ll = long long;

struct seg {
    int n{};
    vector<int> t;
    vector<int> a;

    void init(const vector<int>& b) {
        a = b;
        n = static_cast<int>(a.size());
        t.assign(4 * n, 0);
        build(1, 0, n - 1);
    }

    void build(int v, int l, int r) {
        if (l == r) {
            t[v] = a[l];
            return;
        }
        int m = (l + r) >> 1;
        build(v << 1, l, m);
        build(v << 1 | 1, m + 1, r);
        t[v] = max(t[v << 1], t[v << 1 | 1]);
    }

    int query(int v, int l, int r, int ql, int qr_, int thr) {
        if (qr_ < l || r < ql || t[v] <= thr) return -1;
        if (l == r) return l;
        int m = (l + r) >> 1;
        int res = query(v << 1 | 1, m + 1, r, ql, qr_, thr);
        if (res != -1) return res;
        return query(v << 1, l, m, ql, qr_, thr);
    }

    int query(int l, int r, int thr) {
        if (l > r) return -1;
        return query(1, 0, n - 1, l, r, thr);
    }
};

void solve() {
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        int n, q;
        ll l;
        cin >> n >> q >> l;
        vector<ll> x(n + 1);
        for (int i = 1; i <= n; i++) cin >> x[i];
        vector<pair<ll, int>> vp;
        vp.reserve(n);
        for (int i = 1; i <= n; i++) vp.emplace_back(x[i], i);
        sort(vp.begin(), vp.end());
        vector<ll> p(n);
        vector<int> id(n);
        for (int i = 0; i < n; i++) {
            p[i] = vp[i].first;
            id[i] = vp[i].second;
        }
        seg sgt;
        sgt.init(id);
        set<ll> w;
        w.insert(1);
        w.insert(l);
        ll sum = 0;
        while (q--) {
            int tp;
            cin >> tp;
            if (tp == 1) {
                ll xx;
                cin >> xx;
                w.insert(xx);
            } else {
                int r;
                ll s;
                cin >> r >> s;
                ll xx = x[r];
                auto it = w.upper_bound(xx);
                ll b = *it, a = *prev(it), d = b - a;
                int r2 = static_cast<int>(lower_bound(p.begin(), p.end(), b) - p.begin()) - 1;
                int l2 = static_cast<int>(upper_bound(p.begin(), p.end(), a) - p.begin());
                int any = sgt.query(l2, r2, r);
                if (any == -1) {
                    sum += 0;
                    continue;
                }
                ll k = s / d;
                int ans = -1;
                if (k == 0) {
                    ll y = 2 * (a + s) - xx;
                    int pos = static_cast<int>(upper_bound(p.begin(), p.end(), y) - p.begin()) - 1;
                    int qr_ = min(r2, pos);
                    int res = sgt.query(l2, qr_, r);
                    if (res != -1) ans = id[res];
                    else ans = 0;
                } else {
                    ll rem = s % d;
                    ll y = 2 * (a + rem) - xx;
                    int pos = static_cast<int>(upper_bound(p.begin(), p.end(), y) - p.begin()) - 1;
                    int qr_ = min(r2, pos);
                    int res = sgt.query(l2, qr_, r);
                    if (res != -1) ans = id[res];
                    else ans = id[any];
                }
                sum += (ans < 0 ? 0 : ans);
            }
        }
        cout << "Case #" << tc << ": " << sum << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}

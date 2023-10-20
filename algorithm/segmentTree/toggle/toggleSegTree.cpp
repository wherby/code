// https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/D?source=facebook
// https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/scoreboard?source=facebook
// today_is_gonna_be_a_great_da5y_ ivan_safonov _isaf_source_code
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
#define TIME clock() * 1.0 / CLOCKS_PER_SEC

const int M = 1e6 + 239;
const int T = (1 << 21);
const int MOD = 1e9 + 7;

pair<int, int> mn[T][2];
int add[T];

int n, a[M];
int q;

void build(int i, int l, int r) {
    add[i] = 0;
    if (r - l == 1) {
        mn[i][0] = {a[l], l};
        mn[i][1] = {MOD - a[l], l};
        return;
    }
    int mid = (l + r) / 2;
    build(2 * i + 1, l, mid);
    build(2 * i + 2, mid, r);
    mn[i][0] = min(mn[2 * i + 1][0], mn[2 * i + 2][0]);
    mn[i][1] = min(mn[2 * i + 1][1], mn[2 * i + 2][1]);
}

void push(int i, int l, int r) {
    if (add[i] == 0) {
        return;
    }
    swap(mn[i][0], mn[i][1]);
    if (r - l > 1) {
        add[2 * i + 1] = (add[2 * i + 1] + 1) % 2;
        add[2 * i + 2] = (add[2 * i + 2] + 1) % 2;
    }
    add[i] = 0;
}

void change(int i, int l, int r, int ql, int qr) {
    push(i, l, r);
    if (qr <= l || r <= ql) {
        return;
    }
    if (ql <= l && r <= qr) {
        add[i] = (add[i] + 1) % 2;
        push(i, l, r);
        return;
    }
    int mid = (l + r) / 2;
    change(2 * i + 1, l, mid, ql, qr);
    change(2 * i + 2, mid, r, ql, qr);
    mn[i][0] = min(mn[2 * i + 1][0], mn[2 * i + 2][0]);
    mn[i][1] = min(mn[2 * i + 1][1], mn[2 * i + 2][1]);
}

void solve() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    build(0, 0, n);
    cin >> q;
    ll ans = 0;
    for (int z = 0; z < q; z++) {
        int l, r;
        cin >> l >> r;
        l--;
        change(0, 0, n, l, r);
        ans += mn[0][1].second + 1;
    }
    cout << ans << "\n";
}

int main() {
#ifdef ONPC
    freopen("today_is_gonna_be_a_great_day_input.txt", "r", stdin);
    freopen("answer.txt", "w", stdout);
#endif
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    int TC;
    cin >> TC;
    cerr << TC << " tests" << std::endl;
    for (int i = 0; i < TC; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cerr << "Test case #" << i + 1 << " done!, " << TIME << "s passed" << std::endl;
    }

    return 0;
}

#pragma GCC optimize("Ofast","unroll-all-loops","fast-math","no-stack-protector")
#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#if 1
void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}
template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '['; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "]";}
void _print() {cerr << endl << flush;}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#define DEBUG(x...) cerr << "*["<<__LINE__<<"]\t"<< #x << " = "; _print(x)
template<class T>
istream& operator>>(istream& is, vector<T>& v) {
	int n; is>>n; v.resize(n);
	for(auto &i:v) is>>i;
	return is;
}
template<class T1,class T2>
istream& operator>>(istream& is, pair<T1,T2>& p) {
	is>>p.fi>>p.se;
	return is;
}
template<class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
	for(const auto &i:v) os<<i<<' ';
	return os;
}
template<class T1,class T2>
ostream& operator<<(ostream& os, const pair<T1,T2>& p) {
	os<<p.fi<<' '<<p.se; return os;
}
#endif
 
#define ll long long
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define pi pair<int, int>
#define mod 998244353
template<typename T> bool chkmin(T &a, T b){return (b < a) ? a = b, 1 : 0;}
template<typename T> bool chkmax(T &a, T b){return (b > a) ? a = b, 1 : 0;}
ll ksm(ll a, ll b) {if (b == 0) return 1; ll ns = ksm(a, b >> 1); ns = ns * ns % mod; if (b & 1) ns = ns * a % mod; return ns;}
const int S = pow(7, 7);
const int maxn = 3000005;
struct ST {
    ST *ch[2];
    int l, r;
    pi lst;
}p[maxn << 1], *root;
int stcnt = 0;
void upd(ST *a) {
    a->lst = min(a->ch[0]->lst, a->ch[1]->lst);
}
void bdtree(ST *a, int l, int r) {
    a->l = l, a->r = r;
    if (l == r) {
        a->lst = mp(1e9 + 7, l);
        return ;
    }
    int mid = (l + r) >> 1;
    a->ch[0] = &p[stcnt++];
    a->ch[1] = &p[stcnt++];
    bdtree(a->ch[0], l, mid);
    bdtree(a->ch[1], mid + 1, r);
    upd(a);
}

void upd(ST *a, int pos, int tp) {
    if (a->l == a->r) {
        int oldtp = a->lst.fi;
        if (oldtp > 1e9) oldtp = 0;
        oldtp += tp;
        if (oldtp == 0) oldtp = 1e9 + 7;
        a->lst = mp(oldtp, a->l);
        return ;
    }
    int mid = (a->l + a->r) >> 1;
    if (pos <= mid) upd(a->ch[0], pos, tp);
    else upd(a->ch[1], pos, tp);
    upd(a);
}

int sz[maxn];
int son[maxn];
vi eg[maxn];
int pre[maxn], des[maxn];
int gans() {
    if (root->lst.fi > 1e9) return 0;
    return root->lst.se;
}
int id[maxn];
void dfs1(int a) {
    pre[a] = gans();
    upd(root, id[a], 1);
    for (auto v : eg[a]) 
        dfs1(v);
    upd(root, id[a], -1);
}

void pushall(int a, int tp) {
    upd(root, id[a], tp);
    for (auto v : eg[a])
        pushall(v, tp);
}

void dfs2(int a) {
    for (auto v : eg[a]) {
        if (v == son[a]) continue;
        dfs2(v);
        pushall(v, -1);
    }
    if (son[a]) dfs2(son[a]);
    for (auto v : eg[a]) {
        if (v == son[a]) continue;
        pushall(v, 1);
    }
    des[a] = gans();
    upd(root, id[a], 1);
}

string x[maxn];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; cs++) {
        int n;
        cin >> n;
        for (int i = 1; i <= n; i++) eg[i].clear();
        for (int i = 1; i <= n; i++) {
            int p;
            cin >> p >> x[i];
            if (i == 1) continue;
            eg[p].pb(i);
        }
        // sort x in lexicographical order, remove duplicates
        vector<string> vx;
        for (int i = 1; i <= n; i++) vx.pb(x[i]);
        sort(vx.begin(), vx.end());
        vx.erase(unique(vx.begin(), vx.end()), vx.end());
        for (int i = 1; i <= n; i++) 
            id[i] = lower_bound(vx.begin(), vx.end(), x[i]) - vx.begin() + 1;
        stcnt = 0;
        root = &p[stcnt++];
        bdtree(root, 1, n);

        dfs1(1);
        cerr << "?? " << cs << " DFS1" << endl;
        for (int i = n; i >= 1; i--) {
            sz[i] = 1;
            son[i] = 0;
            for (auto v : eg[i]) {
                sz[i] += sz[v];
                if (sz[v] > sz[son[i]]) son[i] = v;
            }
            // cout << i << ' ' << son[i] << endl;
        }
        dfs2(1);
        ll ans = 0;
        for (int i = 1; i <= n; i++) {
            // cout << "?? " << i << ' ' << pre[i] << ' ' << des[i] << endl;
            ans = ans * (vx.size() + 1) + pre[i]; ans %= mod;
            ans = ans * (vx.size() + 1) + des[i]; ans %= mod;
        }
        cout << "Case #" << cs << ": " << ans << endl;
    }
    return 0;
}
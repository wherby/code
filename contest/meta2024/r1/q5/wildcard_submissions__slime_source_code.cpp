#pragma GCC optimize("Ofast","unroll-all-loops","fast-math","no-stack-protector")
//#include <omp.h>
//#include <bits/stdc++.h>
#include<iostream>
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
#define vi vector<ll>
#define pi pair<int, int>
#define mod 998244353
template<typename T> bool chkmin(T &a, T b){return (b < a) ? a = b, 1 : 0;}
template<typename T> bool chkmax(T &a, T b){return (b > a) ? a = b, 1 : 0;}
ll ksm(ll a, ll b) {if (b == 0) return 1; ll ns = ksm(a, b >> 1); ns = ns * ns % mod; if (b & 1) ns = ns * a % mod; return ns;}
#define vc vector<char>
#define BS bitset<105>
int contra[25][25];
int early[1 << 25];

BS subsetor[1 << 25];
BS x[25];

int pw[105];

char inp[105];

const int MAXMASK = 1 << 16;
const int MAXEARLY = 16;  // 根据实际情况调整
ll precalc[MAXEARLY + 1][MAXMASK];
int cnts[MAXMASK];

void precompute() {
    for (int early = 1; early <= MAXEARLY; early++) {
        for (int mask = 0; mask < MAXMASK; mask++) {
            ll ans = 0, cnt = 0;
            for (int i = 0; i < early && i < 16; i++) {
                if (!(mask & (1 << i))) cnt++;
                ans += pw[cnt];
            }
            precalc[early][mask] = ans % mod;
        }
    }
	for (int i = 0; i < MAXMASK; i++) {
		cnts[i] = 16 - __builtin_popcount(i);
	}
}

int calc(const BS& a, int early) {
    ll ans = 1, cnt = 0;
	// for (int i = 0; i < early; i++) {
	// 	if (!a[i]) cnt++;
	// 	ans += pw[cnt];
	// }
	// return ans;

	int* x=(int*)(void*)(&a);
    for (int i = 0; i < early; i += 16) {
        int chunk = min(16, early - i);
		// for (int j = i; j < i + 16; j++) {
		// 	if (a[j]) submask |= (1 << (j - i));
		// }
		int submask = (x[i / 32] >> (i % 32)) & ((1 << 16) - 1);
        ans = (ans + 1LL * precalc[chunk][submask] * pw[cnt]) % mod;
		cnt += cnts[submask];
    }
    return ans % mod;
}

vector<char> s[25];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	pw[0] = 1;
	for (int i = 1; i < 105; i++) pw[i] = 1ll * pw[i - 1] * 26 % mod;
	precompute();

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
		int n;
		cerr << 1.0 * clock() / CLOCKS_PER_SEC << endl;
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> inp;
			s[i].clear();
			int l = strlen(inp);
			for (int j = 0; j < l; j++) 
				s[i].pb(inp[j]);
			x[i] = BS(); x[i].reset();
			for (int j = 0; j < l; j++)
				if (s[i][j] != '?') x[i][j] = 1;
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				contra[i][j] = min(s[i].size(), s[j].size());
				for (int k = 0; k < contra[i][j]; k++)
					if (s[i][k] != s[j][k] && s[i][k] != '?' && s[j][k] != '?') {
						contra[i][j] = k;
						break;
					}
			}
		subsetor[0] = BS(); subsetor[0].reset();
		early[0] = 1e9;
		for (int i = 1; i < (1 << n); i++) {
			int lowest = __builtin_ctz(i);
			subsetor[i] = subsetor[i ^ (1 << lowest)] | x[lowest];
			if (__builtin_popcount(i) == 1) early[i] = contra[lowest][lowest];
			else {
				int nxt = __builtin_ctz(i ^ (1 << lowest));
				early[i] = min(contra[lowest][nxt], early[i ^ (1 << lowest)]);
				early[i] = min(early[i], early[i ^ (1 << nxt)]);
			}
			
		}

		ll ans = 0;
        for (int i = 1; i < (1 << n); i++) {
            ll w = calc(subsetor[i], early[i]);
            if (__builtin_popcount(i) & 1) ans += w;
            else ans -= w;
        }
		ans %= mod;
		if (ans < 0) ans += mod;
		cout << "Case #" << i << ": " << ans << endl;
	}
    return 0;
}
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
#define vi vector<ll>
#define pi pair<int, int>
#define db double
#define mod 998244353
template<typename T> bool chkmin(T &a, T b){return (b < a) ? a = b, 1 : 0;}
template<typename T> bool chkmax(T &a, T b){return (b > a) ? a = b, 1 : 0;}
ll ksm(ll a, ll b) {if (b == 0) return 1; ll ns = ksm(a, b >> 1); ns = ns * ns % mod; if (b & 1) ns = ns * a % mod; return ns;}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		ll N;
		int P;
		cin >> N >> P;
		auto cost = [&](ll X, int d) {

			db frac = 1.0 * min(d * P, 100) / 100;
			frac = frac + (1 - frac) * X / N;
			return 1 / frac * (d + 1);
		};
		auto chkd = [&](ll X) {
			int bestd = 0; 
			db bestc = 1e18;
			for (int d = 0; d < 101; d++) 
				if (chkmin(bestc, cost(X, d))) bestd = d;
			return bestd;
		};
		ll L = N;
		db ans = 0;
		while (L > 0) {
			ll old = L;
			for (ll j = 60; j >= 0; j--) {
				if (L <= (1ll << j)) continue;
				if (chkd(L - (1ll << j)) == chkd(L)) L -= (1ll << j);
			}
			// cout << L << ' ' << old << endl;
			int d = chkd(L);
			db frac = 1.0 * min(d * P, 100) / 100;
			db C = (d + 1) * N;
			db A = frac * N;
			db B = (1 - frac);
			if (B < 0.001) {
				ans += (C / A) * (old - L + 1);
			}
			else {
				db R = log(A + B * old) / B * C;
				ll S = min(L + (ll)1e7, old);
				db sum = 0;
				db SR = log(A + B * S) / B * C;
				R -= SR;
				for (ll g = L; g <= S; g++) 
					sum += C / (A + B * g);
				ans += sum + R;
			}

			L -= 1;
		}
		printf("Case #%d: %.10f\n", i, ans);
	}
	return 0;
}
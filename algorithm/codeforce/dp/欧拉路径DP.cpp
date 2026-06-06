// https://atcoder.jp/contests/arc219/tasks/arc219_g
// https://atcoder.jp/contests/arc219/editorial/20156
// https://atcoder.jp/contests/arc219/submissions/75702792
// algorithm/codeforce/docs/欧拉路径的DP.md


#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
#define rep(i, l, r) for (ll i = (l); i < (r); ++i)
#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()
using ll = long long;
using ull = unsigned long long;
using ld = long double;
using pl = pair<ll,ll>;
using vi = vector<int>;
using vl = vector<ll>;
using vvl = vector<vector<ll>>;
using vvvl = vector<vector<vector<ll>>>;
template<class T> using pq_ = priority_queue<T, vector<T>, greater<T>>;
using mint=modint998244353;
#define sz(x) (int)(x).size()
typedef pair<int, int> pii;



int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll h,w;
    cin>>h>>w;
    ll c=1;
    ll n;
    cin>>n;
    vl a(n);
    vl b(n);
    map<ll,vector<ll>> mp;
    w--;
    rep(i,0,n){
        cin>>a[i]>>b[i];
        a[i]--;
        b[i]--;
        mp[a[i]].push_back(b[i]);
    }
    ll mae=0;
    vector<ll> dp(6,1000000000000000000);
    dp[0]=0;
    for(auto d:mp){
        vector<ll> u=d.second;
        ll f=d.first;
        ll cu=(f-mae)*c;
        sort(all(u));
        vector<ll> ndp(6,1000000000000000000);
        ll ca=u[u.size()-1]*2;
        ll cb=(w-u[0])*2;
        ll co=w;
        ll cn=min(ca,cb);
        rep(i,0,u.size()-1){
            cn=min(cn,2*w-(u[i+1]-u[i])*2);
        }
        dp[0]+=2*cu;
        dp[1]+=2*cu;
        dp[2]+=2*cu;
        dp[3]+=4*cu;
        dp[4]+=4*cu;
        dp[5]+=4*cu;
        ll cr=0;
        ndp[cr]=min(dp[0]+ca,ndp[cr]);
        ndp[cr]=min(dp[1]+co*2,ndp[cr]);
        ndp[cr]=min(dp[2]+co,ndp[cr]);
        ndp[cr]=min(dp[3]+co*2,ndp[cr]);
        ndp[cr]=min(dp[4]+co*2,ndp[cr]);
        ndp[cr]=min(dp[5]+cn,ndp[cr]);
        cr=1;
        ndp[cr]=min(dp[0]+co*2,ndp[cr]);
        ndp[cr]=min(dp[1]+cb,ndp[cr]);
        ndp[cr]=min(dp[2]+co,ndp[cr]);
        ndp[cr]=min(dp[3]+co*2,ndp[cr]);
        ndp[cr]=min(dp[4]+co*2,ndp[cr]);
        ndp[cr]=min(dp[5]+cn,ndp[cr]);
        cr=2;
        ndp[cr]=min(dp[0]+co,ndp[cr]);
        ndp[cr]=min(dp[1]+co,ndp[cr]);
        ndp[cr]=min(dp[2]+cn,ndp[cr]);
        ndp[cr]=min(dp[3]+co,ndp[cr]);
        ndp[cr]=min(dp[4]+co,ndp[cr]);
        ndp[cr]=min(dp[5]+co,ndp[cr]);
        cr=3;
        ndp[cr]=min(dp[0]+cn,ndp[cr]);
        ndp[cr]=min(dp[1]+co*2,ndp[cr]);
        ndp[cr]=min(dp[2]+co,ndp[cr]);
        ndp[cr]=min(dp[3]+cn,ndp[cr]);
        ndp[cr]=min(dp[4]+co*2,ndp[cr]);
        ndp[cr]=min(dp[5]+cn,ndp[cr]);
        cr=4;
        ndp[cr]=min(dp[0]+co*2,ndp[cr]);
        ndp[cr]=min(dp[1]+cn,ndp[cr]);
        ndp[cr]=min(dp[2]+co,ndp[cr]);
        ndp[cr]=min(dp[3]+co*2,ndp[cr]);
        ndp[cr]=min(dp[4]+cn,ndp[cr]);
        ndp[cr]=min(dp[5]+cn,ndp[cr]);
        cr=5;
        ndp[cr]=min(dp[0]+co*2,ndp[cr]);
        ndp[cr]=min(dp[1]+co*2,ndp[cr]);
        ndp[cr]=min(dp[2]+co,ndp[cr]);
        ndp[cr]=min(dp[3]+co*2,ndp[cr]);
        ndp[cr]=min(dp[4]+co*2,ndp[cr]);
        ndp[cr]=min(dp[5]+cn,ndp[cr]);
        dp=ndp;
        mae=f;
    }
    cout<<min({dp[0],dp[1],dp[5]})<<endl;
}





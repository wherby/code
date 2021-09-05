#include "bits/stdc++.h"
#include "ext/pb_ds/assoc_container.hpp"

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define db puts("*****")
#define mid(x , y) ((x+y)>>1)
#define ff first
#define ss second
#define all(x)  x.begin(),x.end()
#define ll long long
#define sqr(x)  ((x)*(x))
#define pii pair <int , int>
#define sz(x) int(x.size())
#define tr(it , c) for(__typeof(c.begin()) it = (c.begin()); it != (c.end()); it++)
#define y1 you_made_my_day

using namespace std;
using namespace __gnu_pbds;

const int N = 1e6+7;
const int INF = 1e9+7;

template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}
template<class T> bool umod(T& a, T b) { a += b; while(a < 0) a += INF; a %= INF; return 1;}
typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> omar;

int a, b, c, d[N], n, m, vis[N], mx[N], po = 1;
pii p[N];
vector <pii> E[N];
ll T[N<<2], lz[N<<2], ans[N];

void push(int l, int r, int v){
    if(!lz[v])  return;
    
    T[v<<1] += (mid(l, r)-l+1)*lz[v];
    T[v<<1|1] += (r-mid(l, r))*lz[v];
    
    lz[v<<1] += lz[v];
    lz[v<<1|1] += lz[v];
    
    lz[v] = 0;
}

void upd(int x, int y, int l, int r, int v){
    if(y < l || r < x)  return;
    
    if(x <= l && r <= y){
        T[v] += (r-l+1);
        lz[v]++;
        return;
    }
    
    push(l, r, v);
    
    upd(x, y, l, mid(l, r), v<<1);
    upd(x, y, mid(l, r)+1, r, v<<1|1);
    
    T[v] = T[v<<1] + T[v<<1|1];
}

ll get(int x, int y, int l, int r, int v){
    if(y < l || r < x)  return 0;
    
    if(x <= l && r <= y)    return T[v];
    
    push(l, r, v);
    
    return get(x, y, l, mid(l, r), v<<1) + get(x, y, mid(l, r)+1, r, v<<1|1);
}

int main(){
    scanf("%d%d", &n, &m);
    
    for(int i=1; i<=n; i++) scanf("%d", &d[i]);
    for(int i=1; i<=n; i++){
        while(po < n+1 && !vis[d[po]]){
            vis[d[po]]++;
            po++;
        }
        
        mx[i] = po-1;
        vis[d[i]]--;
    }
    
    for(int i=1; i<=m; i++){    
        scanf("%d%d", &p[i].ff, &p[i].ss);
        
        E[p[i].ff].pb(mp(p[i].ss, i));
    }
    
    for(int i=n; i>=1; i--){
        upd(i, mx[i], 1, n, 1);
        
        for(pii j : E[i])
            ans[j.ss] = get(i, j.ff, 1, n, 1);
    }
    
    for(int i=1; i<=m; i++)
        printf("%lld\n", ans[i]);
    
    return 0;
}
//#include <bits/stdc++.h>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <climits>
#include <functional>
#include <cstring>
#include <string>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <random>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/priority_queue.hpp>
#define itn int
#define nit int
#define ll long long
#define ms multiset
#define F(i,a,b) for(register int i=a,i##end=b;i<=i##end;++i)
#define UF(i,a,b) for(register int i=a,i##end=b;i>=i##end;--i)
#define re register
#define ri re int
#define il inline
#define pii pair<int,int>
#define cp complex<double>
#define vi vector<int>
#define ull unsigned long long
#define mem0(x) memset(x,0,sizeof(x))
#define mem0x3f(x) memset(x,0x3f,sizeof(x))
using namespace std;
//using namespace __gnu_pbds;
const double Pi=acos(-1);
namespace fastIO {
	template<class T>
	inline void read(T &x) {
		x=0;
		bool fu=0;
		char ch=0;
		while(ch>'9'||ch<'0') {
			ch=getchar();
			if(ch=='-')fu=1;
		}
		while(ch<='9'&&ch>='0') x=(x*10-48+ch),ch=getchar();
		if(fu)x=-x;
	}
	inline int read() {
		int x=0;
		bool fu=0;
		char ch=0;
		while(ch>'9'||ch<'0') {
			ch=getchar();
			if(ch=='-')fu=1;
		}
		while(ch<='9'&&ch>='0') x=(x*10-48+ch),ch=getchar();
		return fu?-x:x;
	}
	template<class T,class... Args>
	inline void read(T& t,Args&... args) {
		read(t);
		read(args...);
	}
	char _n_u_m_[40];
	template<class T>
	inline void write(T x) {
		if(x==0){
			putchar('0');
			return;
		}
		T tmp = x > 0 ? x : -x ;
		if( x < 0 ) putchar('-') ;
		register int cnt = 0 ;
		while( tmp > 0 ) {
			_n_u_m_[ cnt ++ ] = tmp % 10 + '0' ;
			tmp /= 10 ;
		}
		while( cnt > 0 ) putchar(_n_u_m_[ -- cnt ]) ;
	}
	template<class T>
	inline void write(T x ,char ch) {
		write(x);
		putchar(ch);
	}
}
using namespace fastIO;
int x[1002],l[1002],r[1002],n,p1[1002],p2[1002];
string s[1002];
vector<int>g[1002],gg[1002];
vector<string>ff;
bool vis[1002],bad[1002];
string ans;
inline void dfs(int pos){
	ans+=s[pos];
	for(int i:g[pos])dfs(i);
}
int main() {
	F(iakioi,1,read()){
		memset(vis,0,sizeof(vis));
		mem0(x);mem0(l);mem0(r);mem0(bad);
		F(i,1,n)s[i].clear(),g[i].clear(),gg[i].clear();;ans.clear();
		n=0;
		read(n);
		F(i,1,n)cin>>s[i],s[i].push_back('\0');
		ff.clear();
		F(i,1,n){
			bool tag=false;
			F(j,0,s[i].size()-2)if(s[i][j]!=s[i][j+1]){
				if(!tag){
					if(j!=s[i].size()-2)++l[s[i][j]];
					else ff.push_back(s[i]),bad[i]=true,ff.back().pop_back();
					tag=true;
				}else if(j!=s[i].size()-2){
					++x[s[i][j]];
				}else{
					++r[s[i][j]];
				}
			}
		}
		bool flag=true;F(i,1,n)s[i].pop_back();
		F(i,'A','Z'){
			if(x[i]){
				if(l[i]||r[i]){
					flag=false;
					break;
				}
			}
			if(l[i]>1||r[i]>1){
				flag=false;
				break;
			}
			if(x[i]>1)flag=false;
			string S;S.clear();S.push_back(i);
			if(l[i]&&r[i]){
				int p1=0,p2=0;
				F(j,1,n)if(!bad[j]){
					if(s[j].find(S)!=string::npos){
						if(s[j][0]==S[0])p2=j;
						if(s[j].back()==S[0]) p1=j;
					}
				}
				g[p1].push_back(p2);
				gg[p2].push_back(p1);
			}
		}
		int mmin=1;
		F(i,1,n){
			if(g[i].size()>1||gg[i].size()>1)flag=false;
			if(!g[i].size())mmin=0;
			for(auto j:g[i])vis[j]=true;
		}
		if(mmin)flag=false;
		printf("Case #%d: ",iakioi);
		if(flag){
			F(i,1,n)if(!bad[i]&&!vis[i])dfs(i);
			int sum=0;
			F(i,1,n)sum+=s[i].size();
			for(auto i:ff){
				auto p=ans.find(i[0]);
				if(p==string::npos)ans+=i;
				else
				ans.insert(ans.find(i[0]),i);
			}//cerr<<ans<<endl;
			if(sum!=ans.size())puts("IMPOSSIBLE");
			else cout<<ans<<endl;
		}else puts("IMPOSSIBLE");
	}
	return 0;
}

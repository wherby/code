//https://www.hackerrank.com/rest/contests/w27/challenges/how-many-substrings/hackers/Taaaaaaaaaaaaaaa/download_solution
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N=1e5+5,Q=1e5+5;
#define rank rk
int rank[N],sa[N],height[N];
struct TS
{
	int rank1,rank2,i;
	inline bool operator < (const TS & o) const
	{
		return rank1!=o.rank1?rank1<o.rank1:rank2<o.rank2;
	}
	inline bool operator == (const TS & o) const
	{
		return rank1==o.rank1&&rank2==o.rank2;
	}
};
const int Log=17;
int st[Log][N];
int Lg[N];
inline int getlcp(int l,int r)//l!=r
{
	l=rank[l],r=rank[r];
	if(l>r)swap(l,r);
	int tmp=Lg[r-l];
	return min(st[tmp][l],st[tmp][r-(1<<tmp)]);
}

vector<int> seq[N][2];
int stk[N];
inline bool cmp1(const int &u,const int &v)
{
	return rank[u]<rank[v];
}
inline bool cmp2(const int &u,const int &v)
{
	return rank[u]>rank[v];
}

const int B=300;
//const int B=5;
int delta[N];
LL s[N];
int lcp[N];
int tot;
pair<int,int> event[1005];
inline void update(int x,int len)
{
	if(lcp[x]<len)
	{
		event[tot++]=make_pair(x+lcp[x],-1);
		event[tot++]=make_pair(x+len,1);
		lcp[x]=len;
	}
}

struct QS
{
	int l,r,i;
	inline bool operator < (const QS & o)const
	{
		return l<o.l;
	}
}que[N];
LL ans[N];
int main()
{
	int n,q;
	scanf("%d%d",&n,&q);
	
	{
		static char s[N];
		scanf("%s",s+1);
		for(int i=1;i<=n;++i)rank[i]=s[i]-'a'+1;
		for(int len=1;;len<<=1)
		{
			//printf("---%d---\n",len);
			
			static TS tmp[N];
			for(int i=n;i;--i)tmp[i]=(TS){rank[i],i+len<=n?rank[i+len]:0,i};
			sort(tmp+1,tmp+n+1);
			
			//for(int i=1;i<=n;++i)printf("(%d,%d,%d) ",tmp[i].rank1,tmp[i].rank2,tmp[i].i);
			//puts("");
			
			bool flag=1;
			for(int i=1;i<=n;++i)
				if(tmp[i]==tmp[i-1])
				{
					flag=0;
					rank[tmp[i].i]=rank[tmp[i-1].i];
				}
				else rank[tmp[i].i]=i;
			if(flag)break;
		}
		for(int i=n;i;--i)sa[rank[i]]=i;
		for(int i=1;i<=n;++i)
		{
			height[i]=max(height[i-1]-1,0);
			while(s[sa[rank[i]-1]+height[i]]==s[i+height[i]])++height[i];
		}
	}
	
//	printf("rank=");
//	for(int i=1;i<=n;++i)printf("%d ",rank[i]);
//	puts("");
	
	for(int j=n;--j;)st[0][j]=height[sa[j+1]];
	for(int i=1;n-1>>i;++i)
		for(int j=n-(1<<i);j;--j)
			st[i][j]=min(st[i-1][j],st[i-1][j+(1<<i-1)]);
	for(int i=0,j=1;j<n;++i)
		for(;j<min(n,1<<i+1);++j)
			Lg[j]=i;
	
	{
		int top=0;
		for(int i=n;i;--i)
		{
			//printf("---%d---\n",i);
			
			while(top&&rank[stk[top-1]]<rank[i])--top;
			if(top)seq[i][0].push_back(stk[top-1]);
			stk[top++]=i;
			
			//for(int j=0;j<top;++j)printf("%d ",stk[j]);
			//puts("");
		}
		top=0;
		for(int i=n;i;--i)
		{
			while(top&&rank[stk[top-1]]>rank[i])--top;
			if(top)seq[i][1].push_back(stk[top-1]);
			stk[top++]=i;
		}
	}
	
	{
		vector<int>::iterator it;
		int node;
		for(int i=n;i;--i)
		{
			if(!seq[i][0].empty())
			{
				node=seq[i][0][0];
				for(;;)
				{
					it=lower_bound(seq[node][1].begin(),seq[node][1].end(),i,cmp1);
					if(it==seq[node][1].end())break;
					else
					{
						node=*it;
						seq[i][0].push_back(node);
					}
				}
			}
			if(!seq[i][1].empty())
			{
				node=seq[i][1][0];
				for(;;)
				{
					it=lower_bound(seq[node][0].begin(),seq[node][0].end(),i,cmp2);
					if(it==seq[node][0].end())break;
					else
					{
						node=*it;
						seq[i][1].push_back(node);
					}
				}
			}
			
//			for(int o=0;o<2;++o)
//			{
//				printf("seq(%d,%d)=",i,o);
//				for(int j=0;j<seq[i][o].size();++j)printf("%d ",seq[i][o][j]);
//				puts("");
//			}
		}
	}
	
	for(int i=1;i<=q;++i)
	{
		scanf("%d%d",&que[i].l,&que[i].r);
		++que[i].l,++que[i].r;
		que[i].i=i;
	}
	sort(que+1,que+q+1);
	
	for(int i=n,j=q;i&&j;--i)
	{
//		printf("----%d----\n",i);
		
		event[tot++]=make_pair(i,1);
		for(int k=seq[i][0].size();k--;)update(seq[i][0][k],getlcp(i,seq[i][0][k]));
		for(int k=seq[i][1].size();k--;)update(seq[i][1][k],getlcp(i,seq[i][1][k]));
		
		if(tot>B)
		{
			while(tot--)delta[event[tot].first]+=event[tot].second;
			tot=0;
			int now=0;
			for(int i=1;i<=n;++i)
			{
				now+=delta[i];
				s[i]=s[i-1]+now;
			}
		}
		
//		printf("delta=");
//		for(int k=1;k<=n;++k)printf("%d ",delta[k]);
//		puts("");
//		printf("event=");
//		for(int k=tot;k--;)printf("%d(%d) ",event[k].first,event[k].second);
//		puts("");
		
		for(;que[j].l==i;--j)
		{
			ans[que[j].i]+=s[que[j].r];
			for(int k=tot;k--;)ans[que[j].i]+=event[k].second*max(que[j].r-event[k].first+1,0);
		}
	}
	
	for(int i=1;i<=q;++i)printf("%lld\n",ans[i]);
}
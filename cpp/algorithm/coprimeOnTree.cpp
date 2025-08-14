//https://www.hackerrank.com/rest/contests/w27/challenges/coprime-paths/hackers/h593119681/download_solution
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
#define K 233
#define N 50000+5
#define M 10000000+1
#define mp make_pair

const int Log[8] = {0, 1, 2, 2, 3, 3, 3, 3};
int n,m,depth,l, r, sz, S[9],A[N],Fa[N],p[N][5],T[N], L[N],R[N],q[M],mu[M],F[M],Id[M];
LL ans, Ans[N];
bool Flag[N];
vector <int> Vec[N];

struct Query
{
    int l,r,id;
    void init(int _id){
        scanf("%d%d",&l,&r);
        id = _id;
    }
    bool operator < (const Query a) const
    {
        return mp(L[l]/K,L[r]) < mp(L[a.l]/K,L[a.r]);
    }
}Q[N];

inline void Prepare()
{
	mu[1] = 1;
	for (int i = 2; i < M; i ++)
	{
		if (!F[i])
		{
			F[i] = q[++ q[0]] = i;
			mu[i] = -1;
		}
		for (int j = 1; i * q[j] < M; j ++)
		{
			F[i * q[j]] = q[j];
			if (i % q[j] == 0)
			{
				mu[i * q[j]] = 0;
				break ;
			}
			mu[i * q[j]] = -mu[i];
		}
	}
}


inline void dfs(int z, int fa)
{
    T[++depth] = z;
    for(int i = 0; i < Vec[z].size(); i ++)
    {
        int d = Vec[z][i];
        if (d == fa) continue;
        Fa[d] = z;
        dfs(d,z);
    }
    if(fa)
    {
        T[++depth] = fa;
    }
}


inline void Modify(int x,int op)
{
    sz += op;
    for(int s = 1; s< (1 << p[x][0]); s++)
    {
        int _s = s - (s & -s);
        S[s] = S[_s] *p[x][Log[s&-s]];
        if(op ==1)
        {
            ans +=mu[S[s]] * Id[S[s]];
            Id[S[s]] ++;
        }else
        {
            Id[S[s]] --;
            ans -=mu[S[s]] * Id[S[s]];
        }
    }
}

inline void Deal(int u, int v, int x)
{
    if(v == Fa[u]) swap(u,v);
    if(L[x] >= L[v] && R[x] <=R[v]) Modify(u, Flag[v]? -1: 1);
    else Modify(v ,Flag[v]? -1: 1);
    Flag[v] ^= 1; 
}

int main()
{
    Prepare();
    scanf("%d%d",&n,&m);
    for(int i =1; i <=n; i++)
    {
        scanf("%d",A+i);
        for(int x =A[i]; x > 1; x /=F[x])
        {
            if(Id[F[x]] != i)
            {
                Id[F[x]] = i; 
                p[i][++ p[i][0]] = F[x];
            }
        }
    }
    for(int i = 1; i <M; i++) Id[i] =0;
    for(int i = 1, u,v; i < n; i++){
        scanf("%d%d",&u,&v);
        Vec[u].push_back(v);
        Vec[v].push_back(u);
    }
    dfs(1,0);
    for(int i =1; i <=depth; i++)
    {
        if(!L[T[i]])L[T[i]] = i;
        R[T[i]] = i;
    }
    for(int i =1; i <=m; i++)
    {
        Q[i].init(i);
    }
    sort(Q+1, Q+m+1);
    l=r=S[0] =1;
    Modify(1,1);
    for(int i = 1; i<=m; i++)
    {
        for(;l<L[Q[i].l]; l++) Deal(T[l] ,T[l+1] , T[r]);
        for(;l>L[Q[i].l]; l--) Deal(T[l] ,T[l-1] , T[r]);
        for(;r<L[Q[i].r]; r++) Deal(T[r] ,T[r+1] , T[l]);
        for(;r>L[Q[i].r]; r--) Deal(T[r] ,T[r-1] , T[l]);
        Ans[Q[i].id] = 1LL * sz * (sz-1)/2 + ans;
    }
    for(int i =1; i<=m; i++)
    {
        cout<< Ans[i]<<endl;
    }
    return 0;
}
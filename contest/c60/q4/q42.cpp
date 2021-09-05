class Solution
{
public:
    long long powOf2(int p,int mod)
    {
        if (p==0)
            return(1);
        long long sub=powOf2(p/2,mod);
        sub=sub*sub%mod;
        if (p%2!=0)
            sub=sub*2%mod;
        return(sub);
    }
    
    void dfs(int i,vector<int>& cnt,vector<bool>& inUse,long long& ans,long long curr,int& mod)
    {
        if (i==31)
        {
            ans=(ans+curr)%mod;
            return;
        }
        bool canUse=true;
        if (i%4==0 || i%9==0 || i%25==0)
            canUse=false;
        for (int j=2;j<=i/2;j++)
            if (i%j==0 && inUse[j])
            {
                canUse=false;
                break;
            }
        dfs(i+1,cnt,inUse,ans,curr,mod);
        if (!canUse)
            return;
        inUse[i]=true;
        for (int j=2;j<=i/2;j++)
            if (i%j==0)
                inUse[j]=true;
        dfs(i+1,cnt,inUse,ans,curr*cnt[i]%mod,mod);
        inUse[i]=false;
        for (int j=2;j<=i/2;j++)
            if (i%j==0)
                inUse[j]=false;
    }
    
    int numberOfGoodSubsets(vector<int>& nums)
    {
        int mod=1000000007;
        vector<int> cnt(31,0);
        for (int x:nums)
            cnt[x]++;
        long long ones=powOf2(cnt[1],mod);
        long long ans=0;
        vector<bool> inUse(31,false);
        dfs(2,cnt,inUse,ans,1,mod);
        ans=(ans-1+mod)%mod;
        ans=ans*ones%mod;
        return((int)ans);
    }
};

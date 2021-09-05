//https://discuss.leetcode.com/topic/111241/c-o-n-2-time-o-n-memory-with-explanation
#include<bits/stdc++.h>
using namespace std;

class Solution {

public:
    int countPalindromicSubsequences(string s) {
        int md = 1000000007;
        int n = s.size();
        int dp[3][n][4];
        for (int len = 1; len <=n; ++len) {
            for (int i = 0; i + len <=n; ++i) for (int x = 0; x < 4; ++x)  {
                int &ans = dp[2][i][x];
                ans = 0;
                int j = i + len - 1;
                char c = 'a' + x;
                if (len == 1) ans = s[i] == c;
                else {
                    if (s[i] != c) ans = dp[1][i+1][x];
                    else if (s[j] != c) ans = dp[1][i][x];
                    else {
                        ans = 2;
                        if (len > 2) for (int y = 0; y < 4;++y) {
                            ans += dp[0][i+1][y];
                            ans %=md;
                        }
                    }
                }
            }
            for (int i=0;i<2;++i) for (int j = 0; j < n; ++j) for (int x=0; x < 4;++x)
                dp[i][j][x] = dp[i+1][j][x];
        }
        int ret = 0;
        for (int x = 0; x < 4;++x) ret = (ret + dp[2][0][x]) %md;
        for(int i=0;i<3;i++){
            for(int j=0;j<n;j++)
            {for(int k =0; k<4;k++){
            cout<<dp[i][j][k]<< " ";
            }
            cout<<endl;
        }
        cout<<endl;
        cout<<"          "<<endl;

        }
        return ret;
    }

};

int main(){
    Solution s;
        cout<<s.countPalindromicSubsequences("abcabcabcabcaabcabcabcabcaabcabcabcabca");
    }
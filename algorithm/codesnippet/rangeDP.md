# https://www.youtube.com/watch?v=FLbqgyJ-70I 1:48:29

for(int i = 1; i < =n ; i++>){
    for(int k = 1; k <= min(i,K);k++){
        for(int j =i ; j>=k;j--){
            dp[i][k] = min(dp[i][k], dp[j-1][k-1] + Max[j:i])
        }
    }
}
Ans =dp[N][K]

# https://www.youtube.com/watch?v=FLbqgyJ-70I 2:04:58  length dp

for(int len =1; len <= N; len ++){
    for(int i = 1; i +len -1 <=N ; i ++>){
        int j = i +len -1;
        for(int k = 1; k <=j ; k++>){
            dp[i][j] = min(dp[i][j],k+ max(dp[i][k-1],dp[k+1][j]))
        }
    }
}
Ans = dp[1][N]

# https://www.youtube.com/watch?v=FLbqgyJ-70I 2:18:50 minimum cost to merge stone

for(int len =1; len<= N ; len ++){
    for(int i =1;i+len -1 <=N ; i++){
        int j = i+len -1;
        for(int k = 2; k<=K; k++){
            for(int m = i; m<=j; m ++){
                dp[i][j][k]=min(dp[i][m-1][k-1] + dp[m][j][1])
            }
        }
        dp[i][j][1] = d[i][j][k]  + sum[i:j];
    }
}
return dp[1][N][1];

# https://www.youtube.com/watch?v=FLbqgyJ-70I 2:30:49 01 背包

for(int i=1; i<=N; i++){
    for(int c =1; c<=C ; c++){
        dp[i][c] = max(dp[i-1][c],dp[i-1][c-wi]+ vi)
    }
}

Ans = max(dp[N][c]) for c = 1,2,...C

# target sum 2:37:25  | Last stone weight2 2:40:18

for(int i =1; i<= N ; i++){
    for(int s =-MAX_SUM; s<= MAX_SUM; s++){
        dp[i][s] = dp[i-1][s-num[i]] + dp[i-1][s+num[i]]
    }
}

Ans = dp[N][S]
 
## {dp[0][0]=0, dp[0][c] =NA}

## last stone weight
for(int i=1; i<=N; i++){
    for(int s = -MAX_SUM; s< MAX_SUM; s++){
        dp[i][s] = dp[i-1][s-num[i]] || dp[i-1][s+num[i]]
    }
}

Ans = the first positive s, dp[N][s] ==true

## {dp[0][0] =true, dp[0][s] = false}



# Ones and Zeros 2:44:13

for(int i = 1; i <= N; i ++){
    for(int c1 = 1; c1<= m; c1++){
        for(int c2 =1; c2 <=n; c2++){
            dp[i][c1][c2] = max(dp[i-1][c1][c2], dp[i-1][c1-ai][c2-bi] +1)
        }
    }
}

Ans = max{dp[N][c1][c2]} for c1 <=m, c2<=n

## { dp[0][0][0] = 0, dp[0][c1][c2] = NA}

# LC 879 profitable schemas 2:46:42

for(int i=1;i<=N; i++){
    for(int g =1; g <= MAXG; g ++){
        for(int p =1; p< = MaxP; p++){
            dp[i][g][p] = dp[i-1][g][p] + dp[i-1][g-gi][p-pi]
        }
    }
}


Ans = sum{dp[N][g][p]} for g <=G, p >=p

## 2:50:42
for(int i =1; i<=N; i++){
    for(int g =1; g <=G; g ++){
        for(int p =1 ;p <=P; p++){
            dp[i][g][p] += dp[i-1][g][p];
            dp[i][min(g+gi,G+1)][min(p+pi,P)] += dp[i-1][g][p]
        }
    }
}


Ans = sum{dp[g][P]} for g<=G
## G+1 把所有不符合的都放在同一状态

# LC 956 tallest billboard 3:03:34

for(int i =1; i<=N; i++){
    for(int l =1; l <=MAXL;l++){
        for(int r =1; r<=MAXR; r++){
            if(dp[i-1][l][r] | dp[i-1][l-hi][r] |dp[i-1][l][r-hi]){
                dp[i][l][r]=1
            }
        }
    }
}

Ans = max(l or r) for dp[N][l][r] == 1 and l ==r


## 3:03:47

for(int i =1; i<= N ; i++){
    for(int d = -maxD; d<=maxD,d ++){
        dp[i][d]  = max(dp[i-1][d], dp[i-1][d+h],dp[i-1][d-hi]+hi)
    }
}

dp[i][d] 记录的是左边长度的最大值

Ans = dp[N][0]

# 状态压缩

## LC 691 stickers to spell word 3:08:35

for(int i=1; i<=N; i++){
    for(int set =0; set<=(1<<26)-1; set++){
        dp[i][set] = min(dp[i][set], dp[i-1][set])
        int new_set = unionset(set,word[i])
        dp[i][new_set] = min(dp[i][new_set],dp[i-1][set]+1)
    }
}

Ans = min(dp[N][set])
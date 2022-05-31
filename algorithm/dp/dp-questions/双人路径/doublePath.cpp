// https://www.jianshu.com/p/5adb4c1635c1
#include <cstdio>
#include <algorithm>
#define MAX 9
using namespace std;

int n, g[MAX+1][MAX+1], f[MAX+1][MAX+1][MAX+1][MAX+1];
int main(){
    scanf("%d", &n);
    int x, y, v;
    do{
        scanf("%d%d%d", &x, &y, &v);
        g[x][y] = v;
    } while(x != 0 || y != 0 || v != 0);
    f[1][1][1][1] = g[1][1];
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            for(int k = 1; k <= i + j - 1; k++){
                int l = i + j - k;
                f[i][j][k][l] = max(f[i-1][j][k-1][l], max(f[i-1][j][k][l-1], max(f[i][j-1][k-1][l], f[i][j-1][k][l-1])));
                f[i][j][k][l] += (i == k) ? g[i][j] : g[i][j] + g[k][l];
            }
        }
    }
    printf("%d\n", f[n][n][n][n]);
    return 0;
}
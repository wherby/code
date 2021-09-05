/**  
* 解析： 动态规划。 首先找到子结构，构造递推式。  
* 对于每个位置能获得的最大值是:  
*       a[i][j] = max{a[i-1][j] + w[i][j],a[i][j-1] + w[i][j]}  
*/    
  
  
#include <stdio.h>  
#define N 5  
  
int w[N][N];//每个位置的权值  
int max[N][N];//每个位置获得的最大值  
int path[N][N];//每个位置最大值是从哪个方向获取到的，1是从上方获得，0是从左方获得  
  
void find_path()  
{  
    int i,j;  
    max[0][0] = w[0][0];//初始化  
    path[0][0] = 0;//完全是为了初始化，没什么意义，取1也可以  
    for(i=1;i<N;i++)//初始化第一行  
    {  
        max[0][i] = max[0][i-1]+w[0][i];  
        path[0][i] = 0;  
    }  
    for(i=1;i<N;i++)//初始化第一列  
    {  
        max[i][0] = max[i-1][0]+w[i][0];  
        path[i][0] = 1;  
    }  
    for(i=1;i<N;i++)  
    {  
        for(j=1;j<N;j++)  
        {  
            int down = max[i-1][j] + w[i][j];//从上方获得的最大值与本位置权值的和  
            int right = max[i][j-1] + w[i][j];//从左方获得的最大值与本位置权值的和  
            if(down > right)//比较两个值得大小，取较大值  
            {  
                max[i][j] = down;  
                path[i][j] = 1;//标识获取最大值方向是从上方获取  
            }  
            else  
            {  
                max[i][j] = right;  
                path[i][j] = 0;//标识获取最大值方向是从左方获取  
            }  
        }  
    }  
}  
  
void print_path_core(int i, int j)//打印获取max[N-1][N-1]的路径，从w[N-1][N-1]向上递归到w[0][0]  
{  
    if(i==0 && j==0)//递归到w[0][0]  
    {  
        printf("%d\t",w[i][j]);  
        return;  
    }  
    if(path[i][j]==0)//本位置最大值的获取是从左方获取  
    {  
        print_path_core(i,j-1);//从左面那个值继续递归  
        printf("%d\t",w[i][j]);  
    }  
    else if(path[i][j]==1)//本位置最大值的获取是从上方获取  
    {  
        print_path_core(i-1,j);//从上面那个值继续递归  
        printf("%d\t",w[i][j]);  
    }  
}  
  
void print_path()  
{  
    printf("打印出路径上每个位置所能获得最大值以及所获取的方向(0:从左方获得;1:从上方获得):\n");  
    int i,j;  
    for(i=0;i<N;i++)  
    {  
        for(j=0;j<N;j++)  
            printf("%d(%d)\t",max[i][j],path[i][j]);  
        printf("\n");  
    }  
    printf("\n");  
    printf("从(0,0)到(n,n)所获得的最大值为%d，路径为:\n",max[N-1][N-1]);  
    print_path_core(N-1,N-1);  
    printf("\n");  
}  
  
int main()  
{  
    int a[N][N] = {{4,3,12,1,5},{11,7,4,2,9},{6,20,15,2,8},{4,5,8,1,10},{3,3,4,6,7}};  
    int i,j;  
    printf("矩阵每个位置的权值为:\n");  
    for(i=0;i<N;i++)  
    {  
        for(j=0;j<N;j++)  
        {  
            w[i][j]=a[i][j];  
            printf("%d\t",w[i][j]);  
        }  
        printf("\n");  
    }  
    find_path();  
    print_path();  
    return 0;  
}  
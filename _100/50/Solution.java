class Solution {
    public double myPow(double x, int n) {
        return n>0? helper(x, n):helper(1/x,-n);
    }

    private double helper(double x,int n){
        double res =1;
        while(n>0){
            if(n%2 !=0){
                res = res *x;
            }
            x = x * x;
            n= n/2;
        }
        return res;
    }
}
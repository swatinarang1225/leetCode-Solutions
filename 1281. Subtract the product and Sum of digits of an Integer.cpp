class Solution {
public:
    int subtractProductAndSum(int n) {

        int sum = 0;
        int product = 1;
        while(n){
            int rem = n%10;
            int quo = n/10;

            n = quo;

            sum = sum +rem;
            product *=rem;
        }

        return product-sum;        
    }
};

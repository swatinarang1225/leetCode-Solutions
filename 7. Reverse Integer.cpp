class Solution {
public:
    int reverse(int x) {
        long int ans = 0;
        int i = 0;

        while(x!=0){
          int digit = x%10;
          ans = digit + (ans * 10);
          x = x/10;
          i++;
        }

        if(ans> pow(-2,31) && ans < pow (2,31) -1){
          return ans;
        }
        else{
          return 0;
        }
      
    }
};

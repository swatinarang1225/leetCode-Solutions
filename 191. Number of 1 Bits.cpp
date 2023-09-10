class Solution {
public:
    int hammingWeight(uint32_t n) {
        
        int count = 0;
        while(n){
            int rem = n%2;
            n = n/2;

            if (rem == 1){
                count++;
            }
        }
        return count;
        
    }
};

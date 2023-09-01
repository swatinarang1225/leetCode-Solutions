class Solution {
public:

// Funtion DectoBin converts decimal number to binary and count the '1' in converted binary value.
    int DectoBin( int n){
        int rem;
        int count=0;
        if(n==0){
            return 0;
        }
        while(n!=1){
            rem = n%2;
            if(rem == 1){
                count++;
            }
            n = n/2;}
        if(n==1){
            count++;
        } 
        return count;

    }

    vector<int> countBits(int n) {
        vector<int> v1;
        for(int i = 0; i<=n; i++){
          
            // pushing the returned count value into vector v1.
            v1.push_back(DectoBin(i));
        }
        return v1;
    }
};

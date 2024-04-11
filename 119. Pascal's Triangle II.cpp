class Solution {
public:
    vector<int> getRow(int rowIndex) {

        int arr[rowIndex+1][rowIndex+1];
        vector<int> v1;

        for(int i = 0; i<rowIndex+1; i++){
            for(int j = 0; j<i+1; j++){
                if(j == 0||j==i){
                    arr[i][j] =1;
                
                }
                else{
                    arr[i][j] = arr[i-1][j] + arr[i-1][j-1];
                }
                if(i == rowIndex){
                    v1.push_back(arr[i][j]);
                }
            }
            
        }
        return v1;
        
    }
};

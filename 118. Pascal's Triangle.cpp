class Solution {
public:
    vector<vector<int>> generate(int numRows) {

        vector<vector<int>> v1;
        int arr[numRows][numRows];

        for(int i = 0; i<numRows; i++){
            vector<int> v2;
            for(int j = 0; j<i+1; j++){
                if(j == 0 || j==i){
                    arr[i][j] =1;
                }
                else{
                    arr[i][j] = arr[i-1][j]+arr[i-1][j-1];
                }
                v2.push_back(arr[i][j]);

            }
            v1.push_back(v2);
        }
        return v1;        
    }
};

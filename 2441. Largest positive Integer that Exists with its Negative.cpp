class Solution {
public:
    int findMaxK(vector<int>& nums) {
        int i = 0, j = nums.size()-1;
      
      //sorting the vector
        sort(nums.begin(), nums.end());
      
      //Using the 2-pointers approach to check the negative and positive values.
        while(i<j){
            int max = nums[j];
            int min = nums[i];
            if(max + min == 0){
                return max;
            }
            else if (max < abs(min)){
                i = i+1;
            }
            else{
                j = j-1;
            }
        }
        return -1;
    }
};

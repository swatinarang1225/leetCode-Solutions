class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int i = 0;
        while(i<nums.size()){
            if(nums[i] != i){
                return i;
            }
            i++;
        }
        
        return i;
    }
};

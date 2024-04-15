class Solution {
public:
    void moveZeroes(vector<int>& nums) {

        if(nums.size() >1 ){
        
            int left = 0;
            int right = left+1;

            while(left<right && right<nums.size()){
                if(nums[left] == 0 && nums[right] != 0){
                    int temp = nums[right];
                    nums[right] = nums[left];
                    nums[left] = temp;
                    left++;
                    right++;
                }
                else if(nums[left] == 0 && nums[right] == 0){
                    right++;
                }
                else if ((nums[left] != 0 && nums[right] !=0) || (nums[left]!=0 && nums[right] == 0)){
                    left++;
                    right++;
                }

            }
        }
        
    }
};

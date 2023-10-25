class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> v1;
        set<int> s1;

        for(int i = 0; i<nums.size(); i++){
            if(s1.count(nums[i]) ==1){
                v1.push_back(nums[i]);
            }
            else{
                s1.insert(nums[i]);
            }
        }
        return v1;
        
    }
};

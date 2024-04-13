class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        map<int,int> m1;

        for(int i = 0; i<nums.size(); i++){
            m1[nums[i]]++;
        }
        
        for(auto i = m1.begin(); i!= m1.end(); i++){
            if(i->second >1){
                return true;
            }
        }
        return false;
    }
};

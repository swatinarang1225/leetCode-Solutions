#include<map>
class Solution {
public:
    int majorityElement(vector<int>& nums) {

        map<int, int> m1;
        int max_ele;
        int max_val = INT_MIN;
        for(int i = 0; i<nums.size(); i++){
            m1[nums[i]]++;
        }

        for(auto i = m1.begin(); i != m1.end(); i++){
            if(max_val < i->second){
                max_val = i->second;
                max_ele = i->first;
            }
        }
        return max_ele;
        
    }
};

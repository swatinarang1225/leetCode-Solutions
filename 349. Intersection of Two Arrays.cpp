class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {

        vector<int> ans;
        set<int> s1;
        set<int> s2;

        for(int i = 0; i<nums1.size(); i++){
            s1.insert(nums1[i]);
        }
        for(int i= 0; i<nums2.size(); i++){
            if(s1.count(nums2[i]) == 1){
                s2.insert(nums2[i]);
            }
        }
        for(auto val : s2){
            ans.push_back(val);
        }
        return ans;
        
    }
};

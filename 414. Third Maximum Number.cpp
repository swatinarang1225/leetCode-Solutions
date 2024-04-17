class Solution {
public:
    int thirdMax(vector<int>& nums) {

        sort(nums.begin(),nums.end(), greater<int>());
        map<int,int> m1;
        int count = 0;

        for(int i = 0; i<nums.size(); i++ ){
            m1[nums[i]]++;
        }

        for(auto it = m1.crbegin(); it!=m1.crend(); it++){
            cout<<count<<" "<<it->first<<endl;
            if(count == 2){
                return it->first;
            }
            count++;
            
        }
        
       
    return nums[0];
        

        
    }
};

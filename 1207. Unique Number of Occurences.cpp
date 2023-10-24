class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {

        map<int,int> mp;
        set<int> s1;

        for(int i = 0; i<arr.size(); i++){
            mp[arr[i]]++;
        }

        for(auto i:mp){
            s1.insert(i.second);
        }
       
       return mp.size() == s1.size();

    }
};

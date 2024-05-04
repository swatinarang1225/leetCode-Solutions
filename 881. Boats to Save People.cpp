class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {

        sort(people.begin(),people.end());
        int count = 0;
        int i = 0,j = people.size()-1;


        while(i<=j){
            if(i==j){
                count++;
                break;
            }
            if(people[j] == limit){
                count++;
                j--;
            }
            else if(( people[j]<limit) && (limit - people[j]<people[i])){
                count ++;
                j--;
            }
            if(( people[j]<limit) && (limit - people[j]>=people[i])){
                count++;
                j--;
                i++;
            }
        }
        return count;
        
    }
};

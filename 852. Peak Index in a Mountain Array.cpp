class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {

        int maxi;
        int start = 0, end = arr.size()-1;

        while(start<end){
            int mid = start + (end-start)/2;

            if(arr[mid]<arr[mid+1]){
                start = mid+1;
            }
            else{
                end= mid;
            }
        }
        return end;
    
    }
};

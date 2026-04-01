#include<algorithm>

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> arr = {};
        for(int el1:nums1){
            arr.push_back(el1);
        }
        for(int el2:nums2){
            arr.push_back(el2);
        }
        sort(arr.begin(), arr.end());
        double median = 0;
        if((arr.size() % 2) == 0){
            int ind1 = arr.size()/2;
            int ind2 = arr.size()/2 +1;
            ind1--;
            ind2--;
            median = (arr[ind1]+arr[ind2])/2.0;
        }else{
            int ind = (arr.size()+1)/2;
            ind--;
            median  = arr[ind];

        }
        return median;
    }
};
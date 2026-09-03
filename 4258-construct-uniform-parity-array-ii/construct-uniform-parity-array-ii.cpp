class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int minNum=*min_element(nums1.begin(),nums1.end());
        if(minNum%2){return true;}
        bool odd=false;
        for(int num:nums1){
            if(num%2){odd=true;}
        }

        if(odd){return false;}
        return true;
    }
};
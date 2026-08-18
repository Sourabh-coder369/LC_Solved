class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        // if k==1 , then return the only single occuring interger.
        int n=nums.size();
        int l=nums[0],r=nums[n-1];
        map<int,int> mp;
        for(int num:nums){
            mp[num]+=1;
        }

        if(k==1){
            int maxval=-1;
            for(const auto [k,v]:mp){
                if(v==1){
                    maxval=max(maxval,k);
                }
            }
            return maxval;
        }

        if(k==n){
            return *max_element(nums.begin(),nums.end());
        }

        if(mp[l]==1 && mp[r]==1){return max(l,r);}
        else if(mp[l]==1){return l;}
        else if(mp[r]==1){return r;}
        else{return -1;}
    }
};
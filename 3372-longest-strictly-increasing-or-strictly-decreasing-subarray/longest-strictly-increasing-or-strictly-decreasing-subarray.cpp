class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        // one loop for increasing , one loop for decreasing
        int n=nums.size(),l=0,maxlen=1;
        for(int r=1;r<n;r++){
            if(nums[r]<=nums[r-1]){
                l=r;
            }
            maxlen=max(maxlen,r-l+1);
        }

        l=0;
        for(int r=1;r<n;r++){
            if(nums[r]>=nums[r-1]){
                l=r;
            }
            maxlen=max(maxlen,r-l+1);
        }
        return maxlen;
    }
};
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n=nums.size();
        vector<vector<int>> dp(n,vector<int>(2000+1,0));
        dp[0][1000+nums[0]]+=1;
        dp[0][1000-nums[0]]+=1;
        for(int i=1;i<n;i++){
            for(int tar=0;tar<2001;tar++){
                if(dp[i-1][tar]){
                    if(tar-nums[i]>=0){
                        dp[i][tar-nums[i]]+=dp[i-1][tar];
                    }

                    if(tar+nums[i]<2001){
                        dp[i][tar+nums[i]]+=dp[i-1][tar];
                    }
                }
            }
        }
        return dp[n-1][target+1000];
    }
};
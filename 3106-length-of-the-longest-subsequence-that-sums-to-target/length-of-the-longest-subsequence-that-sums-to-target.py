class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp=[0 for i in range(target+1)]
        dp[0]=1
        for i in range(n):
            for j in range(target-1,-1,-1):
                if(dp[j]>0 and j+nums[i]<=target):
                    dp[j+nums[i]]=max(dp[j+nums[i]],dp[j]+1)
        
        if(dp[target]==0):
            return -1
        return dp[target]-1
        

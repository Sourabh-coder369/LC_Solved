class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pf=[0 for i in range(n)]
        sf=[0 for i in range(n)]
        pf[0]=nums[0]
        for i in range(1,n):
            pf[i]=max(pf[i-1],nums[i])
        
        sf[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            sf[i]=min(sf[i+1],nums[i])
        
        for i in range(n):
            score=pf[i]-sf[i]
            if score<=k:
                return i
        return -1


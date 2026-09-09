class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prev={}
        ans=0
        for x in nums:
            curr={}
            curr[x]=curr.get(x,0)+1
            for val,cnt in prev.items():
                b=val&x
                curr[b]=curr.get(b,0)+cnt

            ans+=curr.get(k,0)
            prev=curr 

        return ans  
            
            
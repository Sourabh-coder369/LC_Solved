class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # so k times the minimum element
        # mx<=k*min
        # i have two path decrease the mx element , or increasr the minimum element
        # two pointer solution 
        # for each corresponding max ele i have to find the required min ele to remove
        nums.sort()
        mi,mx=min(nums),max(nums)
        left,right=0,len(nums)-1
        rem=0
        n=len(nums)
        if mx<=mi*k:
            return 0

        rem=inf
        for i in range(n-1,-1,-1):
            low,high=0,i
            while low<high:
                mid=(low+high)//2
                # print(mid)
                if nums[mid]*k>=nums[i]:
                    high=mid
                else:
                    low=mid+1

            # print(i,low)
            rem=min(rem,n-i-1+low)

        return rem
            
                
                
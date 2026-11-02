class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        def moves(val):
            s=0
            for num in nums:
                s+=abs(val-num)
            return s

        n=len(nums)
        nums.sort()
        nums1=[num for num in nums]
        nums1=list(set(nums1))
        nums1.sort()
        l,r=0,len(nums1)-1
        while(l<r):
            mid=(l+r)//2
            ans1=moves(nums1[mid])
            ans2=moves(nums1[mid+1])
            # print(mid)
            if(ans1<ans2):
                r=mid
            else:
                l=mid+1
        
        return moves(nums1[l])

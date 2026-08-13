class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # maxnumber and no of numbers less than that is a variable
        # 1 2 0
        n=len(nums)
        print(nums)
        for i in range(n):
            idx=nums[i]-1
            # prev=-1
            # print(idx,i)
            while idx>-1 and idx<n and idx!=i and nums[idx]!=idx+1:
                temp=nums[idx]
                nums[idx]=idx+1
                idx=temp-1
                # print(idx)

            
            nums[i]=idx+1
            # print(nums)
        
        for i in range(n):
            if i+1!=nums[i]:
                return i+1
        
        return len(nums)+1

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n=len(nums)
        res=[]
        for i,num in enumerate(nums):
            if num==target:
                res.append(i)
        
        return res
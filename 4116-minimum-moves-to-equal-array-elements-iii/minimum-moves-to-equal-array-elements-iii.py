class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        maxNum=max(nums)

        moves=0
        for num in nums:
            moves+=(maxNum-num)
        
        return moves
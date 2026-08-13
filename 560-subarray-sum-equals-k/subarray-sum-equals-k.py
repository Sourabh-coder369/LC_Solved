class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        s=0
        ss=defaultdict(int)
        ss[0]+=1
        res=0
        # s+something=k
        for i in range(n):
            s+=nums[i]
            # print(ss,k-s)
            # if s==k and nums[i]==k and i>0:
            #     res+=1
            if s-k in ss:
                res+=ss[s-k]
            ss[s]+=1
            # print(ss)
        
        return res
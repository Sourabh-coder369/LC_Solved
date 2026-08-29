power=[]
for i in range(0,26):
    power.append(2**i)
    
class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        def findexp(val):
            p=0
            while p<len(power) and power[p]<=val:
                p+=1

            return p-1
            
        mp={}
        n=len(nums)
        for i in range(26):
            mp[i]=chr(ord('a')+i)

        res=[]
        for i in range(n):
            s=""
            val=nums[i]
            while val>0:
                p=findexp(val)
                s+=mp[p]
                val-=power[p]
            res.append(s)

        return res
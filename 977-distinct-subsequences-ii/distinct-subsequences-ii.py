class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # i need to return the distinct subsequences
        n=len(s)
        dp=[0 for i in range(n)]
        dp[0]=1
        seen=set()
        seen.add(s[0])
        mod=10**9+7
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if s[i]==s[j]:
                    dp[i]+=dp[j]
                    break
                else:
                    dp[i]+=dp[j]
            
            if s[i] not in seen:
                dp[i]+=1
                seen.add(s[i])
        
        # print(dp)
        return sum(dp)%mod
class Solution:
    def numSquares(self, n: int) -> int:
        perfectsq=[]
        for i in range(1,101):
            perfectsq.append(i**2)
        
        dp=[-1 for i in range(n+1)]
        dp[0]=0
        for i in range(len(perfectsq)):
            for j in range(n+1):
                if dp[j]>-1 and j+perfectsq[i]<=n:
                    if dp[j+perfectsq[i]]==-1:
                        dp[j+perfectsq[i]]=dp[j]+1
                    else:
                        dp[j+perfectsq[i]]=min(dp[j+perfectsq[i]],dp[j]+1)
                    
        return dp[n]

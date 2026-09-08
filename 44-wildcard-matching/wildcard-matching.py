class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # b...a...a
        # *?
        # what would be my recursive logic ?
        # dp[i][j]=if there a match for these??
        np,ns=len(p),len(s)
        dp=[[False]*(np+1) for i in range(ns+1)]
        # var=False
        dp[0][0]=True
        for i  in range(np):
            if p[i]=='*':
                dp[0][i+1]=True
            else:
                break
                
        pf=[False for i in range(np+1)]
        pf[0]=True
        for i in range(1,ns+1):
            for j in range(1,np+1):
                if p[j-1]=='*':
                    # print(4)
                    dp[i][j]=dp[i][j] or pf[j-1]
                
                elif p[j-1]=="?":
                    dp[i][j]=dp[i-1][j-1]
                
                elif s[i-1]==p[j-1]:
                    dp[i][j]=dp[i-1][j-1]

                pf[j]=pf[j] or dp[i][j]
            # print(dp[i])
        
        # print(dp)
        return dp[ns][np]
                    

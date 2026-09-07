class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        dp=[0 for i in range(n+1)]
        st=[]
        for i in range(n):
            if s[i]=='(':
                st.append(i)
            else:
                if(not st):
                    continue
                
                lstIdx=st.pop()
                dp[i+1]=2+dp[i]+dp[lstIdx]
        
        return max(dp)


        




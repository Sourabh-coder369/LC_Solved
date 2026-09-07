class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # st keeps tract of indexes
        n=len(s)
        maxlen=0
        st=[-1]
        res=0
        for i in range(n):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if st:
                    res=max(res,i-st[-1])
                else:
                    st.append(i)              
        
        return res


class Solution:
    def countValidSubstrings(self, s: str) -> int:
        def asum(n):
            return (n*(n+1))//2

        prev=-1
        cnt=0
        for curr in range(1,len(s)-1):
            if s[curr]=='b' and s[curr-1]=='a' and s[curr+1]=='c':
                cnt+=asum(curr-prev)-1
                prev=curr-1
        
        curr=len(s)-1
        print(curr,prev)
        cnt+=asum(curr-prev)
        return cnt
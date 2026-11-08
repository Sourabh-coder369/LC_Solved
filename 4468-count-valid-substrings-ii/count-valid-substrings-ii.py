class Solution:
    def countValidSubstrings(self, s: str) -> int:
        # lsta,lstab
        # the logic is 
        # lstabc keeping track is neccesary?? starting index

        def asum(n):
            return n*(n+1)//2
        
        n=len(s)
        cnt=0
        lsta,lstab,lstabc=-1,-1,-1
        for curr in range(n):
            if s[curr]=='a':
                lsta=curr

            if s[curr]=='b':
                lstab=lsta
            
            if s[curr]=='c':
                lstabc=lstab
            
            cnt+=curr-lstabc
        
        return cnt
class Solution:
    def numOfSubsequences(self, s: str) -> int:
    # for T inserting no of LC Comb present before 
    # for T

    # initial Count
        n=len(s)
        initialCnt=0
        lCnt,lcCnt=0,0
        maxseq=0
        for c in s:
            if c=='L':
                lCnt+=1
            
            elif c=='T':
                initialCnt+=lcCnt

            elif c=='C':
                lcCnt+=lCnt
            
            maxseq=max(maxseq,lcCnt)

        print(maxseq)
        # for L
        tCnt,ctCnt=0,0
        for c in s[::-1]:
            if c=='T':
                tCnt+=1

            elif c=='C':
                ctCnt+=tCnt
            
            maxseq=max(maxseq,ctCnt)
            
        print(maxseq)
        t=[0 for i in range(n)]
        l=[0 for i in range(n)]

        t[n-1]=1 if s[n-1]=='T' else 0
        l[0]=1 if s[0]=='L' else 0
        for i in range(1,n):
            temp=1 if s[i]=='L' else 0
            l[i]=l[i-1]+temp
        
        for i in range(n-2,-1,-1):
            temp=1 if s[i]=='T' else 0
            t[i]=t[i+1]+temp
        
        for i in range(n-1):
            maxseq=max(maxseq,l[i]*t[i+1])

        print(l,t)
        print(initialCnt,maxseq)
        return initialCnt+maxseq

        
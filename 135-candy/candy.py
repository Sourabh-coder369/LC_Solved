class Solution:
    def candy(self, ratings: List[int]) -> int:
        # peak problem , upward peak is easy , how you solve downward peak 
        n=len(ratings)
        if n==1:
            return 1

        sf=[0 for i in range(n)]
        sf[n-1]=1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                sf[i]=sf[i+1]+1
            else:
                sf[i]=1
        
        print(sf)
        res=[0 for i in range(n)]
        inc=False
        if ratings[0]==ratings[1]:
            res[0]=1
        elif ratings[0]>ratings[1]:
            res[0]=sf[0]
        else:
            res[0]=1


        for i in range(1,n):
            if i>0 and ratings[i]==ratings[i-1] and sf[i]<2:
                res[i]=1

            elif i>0 and ratings[i]>ratings[i-1]:
                if sf[i]>1:
                    res[i]=max(res[i-1]+1,sf[i])
                else:
                    res[i]=res[i-1]+1
                inc=True

            elif ratings[i]==ratings[i-1]:
                res[i]=sf[i]

            elif inc:
                res[i]=sf[i]
                inc=False

            else:
                res[i]=res[i-1]-1

        print(res)
        return sum(res)
            

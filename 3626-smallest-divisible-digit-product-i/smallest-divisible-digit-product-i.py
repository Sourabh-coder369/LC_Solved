class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            mul=1
            for c in str(i):
                mul*=int(c)
            
            print(mul,i,t)
            if mul%t==0 or mul==0:
                return i
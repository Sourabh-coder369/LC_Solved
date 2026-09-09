class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        pq=deque([])
        n,m=len(grid),len(grid[0])
        dist=[[inf for i in range(m)] for i in range(n)]
        op=0
        pq.append((0,0,grid[0][0]))
        mincst=inf
        print(n-1,m-1)
        while pq and op<=k+1:
            # print(pq)
            for _ in range(len(pq)):
                x,y,cst=pq.popleft()
                if x==n-1 and y==m-1:
                    mincst=min(mincst,cst)
                    continue

                pfsum=0
                for i in range(y-1,-1,-1):
                    pfsum+=grid[x][i]
                    if cst+pfsum>=dist[x][i]:
                        # break
                        continue

                    dist[x][i]=pfsum+cst
                    pq.append((x,i,cst+pfsum))
                
                pfsum=0
                for i in range(y+1,m):
                    pfsum+=grid[x][i]
                    if cst+pfsum>=dist[x][i]:
                        # break
                        continue
                    
                    dist[x][i]=pfsum+cst
                    pq.append((x,i,cst+pfsum))
                
                pfsum=0
                for i in range(x-1,-1,-1):
                    pfsum+=grid[i][y]
                    if cst+pfsum>=dist[i][y]:
                        # break
                        continue

                    dist[i][y]=cst+pfsum
                    pq.append((i,y,cst+pfsum))

                pfsum=0
                for i in range(x+1,n):
                    pfsum+=grid[i][y]
                    if cst+pfsum>=dist[i][y]:
                        # break
                        continue

                    dist[i][y]=cst+pfsum
                    pq.append((i,y,cst+pfsum))

            print(pq)
            op+=1

        if(mincst==inf):
            return -1

        return mincst
                



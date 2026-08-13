class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        
        n,m=len(grid),len(grid[0])
        q=deque([])
        q.append((0,0,1))
        direction=[(0,1),(-1,0),(1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        visited=[[0 for i in range(m)] for i in range(n)]
        visited[0][0]=1
        while q:
            # print(q)
            r,c,d=q.popleft()
            if r==n-1 and c==m-1:
                return d
            
            for dr,dc in direction:
                nr,nc=r+dr,c+dc
                # print(nr,nc)
                if nr<n and nc<m and nr>-1 and nc>-1 and not visited[nr][nc] and grid[nr][nc]==0:
                    visited[nr][nc]=1
                    q.append((nr,nc,d+1))

        return -1
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # topological sorting
        mp=defaultdict(list)
        indeg=defaultdict(int)
        for u,v in invocations:
            mp[u].append(v)
            indeg[v]+=1
        
        q=deque([k])
        sus=set()
        x=set()
        x.add(k)
        while q:
            nd=q.popleft()
            sus.add(nd)
            for v in mp[nd]:
                indeg[v]-=1
                if v not in x:
                    x.add(v)
                    q.append(v)
        
        res=[]
        for i in range(n):
            if i in sus and indeg[i]>0:
                return [i for i in range(n)]

            if i not in sus:
                res.append(i)
        return res


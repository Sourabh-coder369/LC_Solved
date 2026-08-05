class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # simple dfs
        # insted of a character number i return an array(int) which shows the the count of each character
        def dfs(nd):
            ans1=[0 for i in range(26)]
            ans1[ord(labels[nd])-ord('a')]+=1
            for v in mp[nd]:
                if not visited[v]:
                    visited[v]=1
                    s=dfs(v)
                    for i in range(26):
                        ans1[i]+=s[i]
            
            res[nd]=ans1[ord(labels[nd])-ord('a')]
            # print(nd,ans1)
            return ans1

        
        
        mp=defaultdict(list)
        res=[0 for i in range(n)]
        print(ord(labels[0])-ord('a'))
        for u,v in edges:
            mp[u].append(v)
            mp[v].append(u)
        

        visited=[0 for i in range(n)]
        visited[0]=1
        dfs(0)
        return res

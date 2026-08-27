class dsu{
    public:
    vector<int> parent;
    vector<int> rank;

    dsu(int n){
        parent.resize(n);
        rank.resize(n,0);
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
    }
    
    int find(int nd){
        if(parent[nd]!=nd){
            parent[nd]=find(parent[nd]);
        }
        return parent[nd];
    }

    bool unite(int x,int y){
        int u=find(x);
        int v=find(y);

        if(u==v){return false;}
        
        if(rank[u]<rank[v]){
            parent[u]=v;
        }
        else if(rank[u]>rank[v]){
            parent[v]=u;
        }
        else{
            parent[v]=u;
            rank[u]++;
        }

        return true;
    }
};

class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, int k) {
        // see does removing a edge keeps the component connected
        // how to track the connected components ?
        int mxt=1e+9+1,low=0,high=mxt,m=edges.size(),components=n;
        while(low<high){
            int mid=(low+high)/2;
            int components=n;
            dsu d(n);
            for(int i=0;i<m;i++){
                if(edges[i][2]>mid){
                    bool val=d.unite(edges[i][0],edges[i][1]);
                    if(val){components--;}
                }
            }

            if(components>=k){
                high=mid;
            }
            else{
                low=mid+1;
            }
        }
        return low;
    }
};
class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int n=classroom.size(),m=classroom[0].size();
        int sr,sc,k=0;
        vector<vector<int>> id(n,vector<int>(m,0));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(classroom[i][j]=='S'){
                    sr=i;
                    sc=j;
                }
                else if(classroom[i][j]=='L'){
                    id[i][j]=k;
                    k++;
                }
            }
        }
        // k--;
        struct state{
            int x,y,moves,energy,mask;
        };

        vector<vector<vector<int>>> best(n,vector<vector<int>>(m,vector<int>(1<<k,-1)));
        deque<state> q;
        best[sr][sc][0]=energy;
        q.push_back({sr,sc,0,energy,0});
        vector<pair<int,int>> coord={{0,1},{1,0},{-1,0},{0,-1}};

        while(!q.empty()){
            state cur=q.front();
            if(cur.mask==(1 << k) - 1){
                return cur.moves;
            }
            q.pop_front();
            for(auto& [dx,dy] : coord){
                state nxt = cur;

                nxt.x += dx;
                nxt.y += dy;

                if(nxt.x < 0 || nxt.y < 0 || nxt.x >= n || nxt.y >= m){
                    continue;
                }

                if(classroom[nxt.x][nxt.y] == 'X'){
                    continue;
                }

                nxt.energy--;

                if(nxt.energy < 0){
                    continue;
                }

                if(classroom[nxt.x][nxt.y] == 'R'){
                    nxt.energy = energy;
                }

                if(classroom[nxt.x][nxt.y] == 'L'){
                    nxt.mask |= 1 << (id[nxt.x][nxt.y]);
                }

                if(best[nxt.x][nxt.y][nxt.mask] >= nxt.energy){
                    continue;
                }

                nxt.moves++;
                best[nxt.x][nxt.y][nxt.mask] = nxt.energy;
                q.push_back(nxt);
            }
        }

        return -1;
    }
};
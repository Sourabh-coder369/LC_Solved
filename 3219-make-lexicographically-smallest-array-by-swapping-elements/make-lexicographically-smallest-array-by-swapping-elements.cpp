class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        //i think that's the approach 
        int n=nums.size();
        vector<vector<int>> copy;
        for(int i=0;i<n;i++){
            copy.push_back({nums[i],i});
        }

        sort(copy.begin(),copy.end());
        priority_queue<int,vector<int>,greater<int>> pq;
        vector<int> res(n,0);
        int begin=0;
        pq.push(copy[0][1]);
        // for(int i=0;i<n;i++){
        //     cout<<copy[i][0]<<"-"<<copy[i][1]<<" ";
        // }
        // cout<<endl;
        for(int i=1;i<n;i++){
            if(copy[i][0]-copy[i-1][0]>limit){
                while(!pq.empty()){
                    // cout<<pq.top()<<" ";
                    res[pq.top()]=copy[begin][0];
                    pq.pop();
                    begin++;
                    
                }
                // cout<<endl;
            }
            pq.push(copy[i][1]);
        }

        while(!pq.empty()){
            // cout<<pq.top()<<" ";
            res[pq.top()]=copy[begin][0];
            pq.pop();
            begin++;
        }
        // cout<<endl;
        
        return res;
    }
};
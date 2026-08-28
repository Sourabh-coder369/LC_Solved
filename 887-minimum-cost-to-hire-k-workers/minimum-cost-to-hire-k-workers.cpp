class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        vector<pair<double,int>> arr;
        for(int i=0;i<wage.size();i++){
            arr.push_back({(double)wage[i]/quality[i],i});
        } 
        sort(arr.begin(),arr.end());
        priority_queue<int> pq;
        int q=0;
        double mincst=DBL_MAX;
        for(int i=0;i<arr.size();i++){
            q+=quality[arr[i].second];
            pq.push(quality[arr[i].second]);
            if(pq.size()>k){
                q-=pq.top();
                pq.pop();
            }

            if(pq.size()==k){
                mincst=min(mincst,arr[i].first*q);
            }           
        }
        return mincst;
    }
};
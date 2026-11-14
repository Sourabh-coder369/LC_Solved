class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        // the point is i always pick the next available server , 
        using p=pair<long long,int>;
        priority_queue<p,vector<p>,greater<p>> busy;
        priority_queue<int,vector<int>,greater<int>> free;
        for(int i=0;i<k;i++){
            free.push(i);
        }
        vector<int> count(k,0);
        int req=arrival.size();
        for(int i=0;i<req;i++){
            while(busy.size()>0 && busy.top().first<=arrival[i]){
                int server=busy.top().second;
                int virId=i+(server-i%k+k)%k;
                free.push(virId);
                busy.pop();
            }
            if(free.size()>0){
                int virId=free.top();
                free.pop();
                busy.push({(long long)arrival[i]+load[i],virId%k});
                count[virId%k]++;
            }   
        }

        int mxused=*max_element(count.begin(),count.end());
        vector<int> res;
        for(int i=0;i<k;i++){
            if(count[i]==mxused){
                res.push_back(i);
            }
        }

        return res;
    }
};
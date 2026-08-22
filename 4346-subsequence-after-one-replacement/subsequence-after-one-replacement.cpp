class Solution {
public:
    bool canMakeSubsequence(string s, string t) {
        int n=s.size(),m=t.size();
        vector<int> sf(n,-1);
        vector<int> pf(n,m);
        if(n==1){return true;}
        if(n>m){return false;}
        
        int idx=n-1;
        for(int i=m-1;i>-1;i--){
            if(s[idx]==t[i]){sf[idx]=i;idx--;}
            if(idx==-1){break;}
        }

        idx=0;
        for(int i=0;i<m;i++){
            if(s[idx]==t[i]){pf[idx]=i;idx++;}
            if(idx==n){break;}
        }

        // for(int i=0;i<n;i++){
        //     cout<<pf[i]<<" ";
        // }
        // cout<<endl;

        // for(int i=0;i<n;i++){
        //     cout<<sf[i]<<" ";
        // }
        // cout<<endl;

        for(int i=0;i<n;i++){
            if(i==0 && i+1<n){
                if(sf[i+1]>0){return true;}
            }
            else if(i==n-1 && i-1>-1){
                if(pf[i-1]<m-1){return true;}
            }
            else{
                if(sf[i+1]-pf[i-1]>1 && sf[i+1]>-1 && pf[i-1]<m){return true;}
            }
        }
        return false;

    }
};
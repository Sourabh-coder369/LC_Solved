class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n=strs.size(),minsize=INT_MAX;
        // vector<int> indexes(n,0);
        string s;
        for(int i=0;i<n;i++){
            if (minsize>strs[i].size()){
                minsize=strs[i].size();
                s=strs[i];
            }
        }

        for(int i=0;i<minsize;i++){
            bool check=true;
            for(int j=1;j<n;j++){
                if(strs[j][i]!=strs[j-1][i]){
                    check=false;
                }
            }
            if(!check){return s.substr(0,i);}
        }
        cout<<s<<" "<<minsize<<endl;
        return s;
        
    }
};
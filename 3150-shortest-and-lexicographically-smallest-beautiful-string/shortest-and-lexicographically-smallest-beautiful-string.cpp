class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n=s.size();
        int left=0,right=0;
        int ones=0,minlen=INT_MAX;
        string res="";
        while(right<n && ones<k){
            if (s[right]=='1'){
                if(ones==k-1){break;}
                ones++;
            }
            right++;
        }        

        if(ones<k-1){return "";}
        while(right<n){    
            if(s[right]=='1'){ones++;}
            while(ones>=k){
                if(s[left]=='1'){ones--;}
                cout<<s.substr(left,right-left+1)<<endl;
                if(right-left+1==minlen && res>s.substr(left,right-left+1)){
                    res=s.substr(left,right-left+1);
                }

                if(right-left+1<minlen){
                    minlen=right-left+1;
                    res=s.substr(left,right-left+1);
                }
                left++;
            }
            right++;  
        }  

        return res;
    }
};
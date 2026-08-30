class Solution {
public:
    bool isPalindrome(int l,int r,string s){
        while(l<r){
            if(s[l]!=s[r]){break;}
            l++;
            r--;
        }
        return l>=r ? true : false; 
    }
    bool validPalindrome(string s) {
        int n=s.size();
        int l=0,r=n-1;

        while(l<r){
            if(s[l]!=s[r]){
                bool ans=isPalindrome(l,r-1,s) || isPalindrome(l+1,r,s);
                if(ans){return true;}
                else{return false;}
            }
            l++;
            r--;
        }

        if(l>=r){return true;}
        return false;
    }
};
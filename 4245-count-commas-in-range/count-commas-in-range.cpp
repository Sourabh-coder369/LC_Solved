class Solution {
public:
    int countCommas(int n) {
        int ans=n/1000;
        if(n<1000){
            return 0;
        }
        return 1+(ans-1)*1000+n%1000;
    }
};
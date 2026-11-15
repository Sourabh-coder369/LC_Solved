class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        // odd-even pairs i should find,
        // even-even is even , even-odd is odd 
        long long mod=1e9+7;
        int oddCnt=0,evenCnt=1;
        int res=0,s=0;
        for(int i=0;i<arr.size();i++){
            s+=arr[i];
            if(s%2==0){
                res+=oddCnt;
                evenCnt++;
            }
            else{
                res+=evenCnt;
                oddCnt++;
            }
            res=res%mod;
        }
        return res;

    }
};
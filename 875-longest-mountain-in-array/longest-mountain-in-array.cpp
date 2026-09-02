class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int n=arr.size();
        if(n<3){
            return 0;
        }
        vector<int> inc(n,1);
        vector<int> dec(n,1);
        int streak=1;
        for(int i=1;i<n;i++){
            if(arr[i]>arr[i-1]){
                streak++;
            }
            else{
                streak=1;
            }
            inc[i]=streak;
        }

        streak=1;
        for(int i=n-2;i>-1;i--){
            if(arr[i]>arr[i+1]){
                streak++;
            }
            else{
                streak=1;
            }
            dec[i]=streak;
        }
        
        int mount=0;
        for(int i=1;i<n-1;i++){
            cout<<inc[i]<<" "<<dec[i];
            if(inc[i]>1 && dec[i]>1 && inc[i]+dec[i]-1>2){
                mount=max(mount,inc[i]+dec[i]-1);
            }
        }

        return mount;

    }
};
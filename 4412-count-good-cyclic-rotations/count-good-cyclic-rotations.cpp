class Solution {
public:
    int countGoodRotations(vector<int>& nums) {
        // way simpler method to do this
        int n=nums.size();
        long long totalsum=0;
        vector<long long> pf(n,0);
        vector<long long> sf(n,0);
        pf[0]=nums[0];
        totalsum+=nums[0];
        for(int i=1;i<n;i++){
            pf[i]=pf[i-1]+nums[i];
            totalsum+=nums[i];
        }

        sf[n-1]=nums[n-1];
        for(int i=n-2;i>-1;i--){
            sf[i]=sf[i+1]+nums[i];
        }

        int ans=0;
        for(int i=-1;i<n/2;i++){
            long long leftsum=0,rightsum=0;

            if(i>-1){leftsum=pf[i];}
            if((n/2)+i+1<n){rightsum=sf[(n/2)+i+1];}

            long long right=leftsum+rightsum;
            cout<<right<<endl;
            if(totalsum-right>right){ans++;}
        }

        cout<<"--"<<endl;
        if(n>2){
            for(int i=1;i<n/2;i++){
                long long leftsum=0;
                if((n/2)+i<n){
                    leftsum+=pf[n-1]-pf[(n/2)+i-1];
                }

                if(i-1>-1){
                    leftsum+=pf[i-1];
                }

                cout<<leftsum<<" "<<totalsum<<endl;
                if(leftsum>totalsum-leftsum){
                    ans++;
                }
            }
        }

        return ans;


    }
};